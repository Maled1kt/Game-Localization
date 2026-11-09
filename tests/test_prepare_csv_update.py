import csv
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest


UPDATER = Path(__file__).resolve().parents[1] / "game-localization" / "scripts" / "prepare_csv_update.py"


class PrepareCsvUpdateTests(unittest.TestCase):
    def setUp(self):
        directory = TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.folder = Path(directory.name)
        self.previous = self.folder / "previous.csv"
        self.current = self.folder / "current.csv"
        self.accepted = self.folder / "accepted.csv"
        self.editor = self.folder / "editor.csv"
        self.output = self.folder / "update.draft.csv"

    def write_csv(self, path, rows, *, source=False):
        headers = ("ID", "EN", "SCENE", "CONTEXT") if source else ("ID", "DE")
        with path.open("w", encoding="utf-8-sig", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(headers)
            writer.writerows(rows)

    def prepare(self, *, editor=True):
        command = [
            sys.executable, "-B", str(UPDATER), str(self.previous), str(self.current),
            str(self.accepted), str(self.output), "--id-column", "ID", "--source-column", "EN",
            "--target-column", "DE", "--scene-column", "SCENE", "--compare-column", "CONTEXT",
            "--delimiter", "semicolon",
        ]
        if editor:
            command.extend(("--editor", str(self.editor)))
        return subprocess.run(command, capture_output=True, text=True, check=False)

    def draft(self):
        with self.output.open(encoding="utf-8", newline="") as file:
            return list(csv.reader(file, delimiter=";"))

    def test_comparison_preserves_edits_and_groups_review_by_scene(self):
        before = [
            ("001", "Stay close.", "Docking", "Crew"),
            ("DIA_002", "Open the airlock.", "Docking", "Crew"),
            ("DIA_003", "Go to the bridge.", "Bridge", "Crew"),
            ("DIA_005", "Ready?", "Docking", "Crew"),
            ("DIA_006", "Go ahead.", "Docking", "Crew"),
            ("MENU_001", "New game", "", ""),
        ]
        after = [
            before[-1], before[0],
            ("DIA_002", "Close the airlock.", "Docking", "Crew"),
            ("DIA_004", "Check the controls.", "Control room", "Crew"),
            ("DIA_005", "Ready?", "Docking", "Pilot"),
            ("DIA_006", "Go ahead.", "Control room", "Crew"),
        ]
        self.write_csv(self.previous, before, source=True)
        self.write_csv(self.current, after, source=True)
        self.write_csv(self.accepted, [
            ("001", "Bleib bei mir."), ("MENU_001", "Neues Spiel"),
            ("DIA_002", "Öffne die Luftschleuse."), ("DIA_003", "Geh zur Brücke."),
            ("DIA_005", "Bereit?"), ("DIA_006", "Nur zu."),
        ])
        edited = 'Bleib hier; "ganz nah".\nBei mir.'
        self.write_csv(self.editor, [
            ("DIA_002", "Mach die Luftschleuse auf."), ("001", edited), ("DIA_004", "Sieh nach."),
        ])
        inputs = {path: path.read_bytes() for path in self.folder.iterdir()}

        result = self.prepare()
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["status"], "needs_review")
        self.assertEqual(report["source_changes"], {"unchanged": 2, "modified": 3, "added": 1, "removed": 1})
        self.assertEqual(report["translation_statuses"], {
            "reused": 1, "preserved_editor": 1, "needs_review": 4, "removed": 1,
        })
        self.assertEqual(self.draft(), [
            ["ID", "DE"], ["MENU_001", "Neues Spiel"], ["001", edited],
            ["DIA_002", ""], ["DIA_004", ""], ["DIA_005", ""], ["DIA_006", ""],
        ])
        rows = {row["id"]: row for row in report["rows"]}
        self.assertEqual(rows["DIA_002"]["prior_translation"], "Öffne die Luftschleuse.")
        self.assertEqual(rows["DIA_002"]["editor_translation"], "Mach die Luftschleuse auf.")
        self.assertEqual(rows["DIA_003"]["prior_translation"], "Geh zur Brücke.")
        self.assertEqual(rows["DIA_004"]["editor_translation"], "Sieh nach.")
        self.assertEqual(rows["DIA_005"]["changed_columns"], {"CONTEXT": {"previous": "Crew", "current": "Pilot"}})
        self.assertEqual(rows["DIA_006"]["changed_columns"], {"SCENE": {"previous": "Docking", "current": "Control room"}})
        scenes = {row["scene"]: row for row in report["scenes"]}
        self.assertEqual(scenes["Docking"]["review_ids"], ["DIA_002", "DIA_005"])
        self.assertEqual(scenes["Control room"]["review_ids"], ["DIA_004", "DIA_006"])
        self.assertEqual(scenes["Bridge"]["removed_ids"], ["DIA_003"])
        self.assertEqual({path: path.read_bytes() for path in inputs}, inputs)

    def test_editor_clear_and_token_error_do_not_fall_back_to_accepted_text(self):
        source = [("A", "Hi {name}", "Docking", ""), ("B", "Back", "Docking", ""), ("C", "Ready?", "Docking", "")]
        self.write_csv(self.previous, source, source=True)
        self.write_csv(self.current, source, source=True)
        self.write_csv(self.accepted, [("A", "Hallo {name}"), ("B", "Zurück")])
        self.write_csv(self.editor, [("A", "Hallo"), ("B", "")])

        result = self.prepare()
        self.assertEqual(result.returncode, 0, result.stderr)
        rows = {row["id"]: row for row in json.loads(result.stdout)["rows"]}
        self.assertEqual(rows["A"]["issues"], [{"code": "protected_tokens", "missing": {"{name}": 1}, "unexpected": {}}])
        self.assertEqual(rows["A"]["editor_translation"], "Hallo")
        self.assertEqual(rows["B"]["reason"], "blank_editor_translation")
        self.assertEqual(rows["B"]["editor_translation"], "")
        self.assertEqual(rows["C"]["reason"], "missing_translation")
        self.assertEqual(self.draft(), [["ID", "DE"], ["A", ""], ["B", ""], ["C", ""]])

    def test_rejects_invalid_ids_without_creating_a_draft(self):
        source = [("A", "Back", "Docking", "")]
        self.write_csv(self.previous, source, source=True)
        self.write_csv(self.accepted, [("A", "Zurück")])
        for invalid, message in ((source + source, "Duplicate ID"), ([("", "Back", "Docking", "")], "Blank ID")):
            with self.subTest(message=message):
                self.write_csv(self.current, invalid, source=True)
                result = self.prepare(editor=False)
                self.assertEqual(result.returncode, 2)
                self.assertIn(message, result.stderr)
                self.assertFalse(self.output.exists())
        self.write_csv(self.current, source, source=True)
        self.write_csv(self.editor, [("UNKNOWN", "Neu")])
        result = self.prepare()
        self.assertEqual(result.returncode, 2)
        self.assertIn("Unexpected translation IDs: UNKNOWN", result.stderr)
        self.assertFalse(self.output.exists())

    def test_reuses_accepted_without_editor_and_protects_existing_draft(self):
        source = [("A", "Back", "Docking", "")]
        self.write_csv(self.previous, source, source=True)
        self.write_csv(self.current, source, source=True)
        self.write_csv(self.accepted, [("A", "Zurück")])

        result = self.prepare(editor=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["status"], "prepared")
        self.assertEqual(self.draft(), [["ID", "DE"], ["A", "Zurück"]])
        previous_draft = self.output.read_bytes()
        result = self.prepare(editor=False)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(self.output.read_bytes(), previous_draft)


if __name__ == "__main__":
    unittest.main()
