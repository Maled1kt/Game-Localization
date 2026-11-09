import copy
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest


HELPER = Path(__file__).resolve().parents[1] / "game-localization" / "scripts" / "prepare_steam_store.py"
SHORT = "app[content][short_description]"
ABOUT = "app[content][about]"
ASSET = "[img]{STEAM_APP_IMAGE}/extras/repair.png[/img]"


class PrepareSteamStoreTests(unittest.TestCase):
    def setUp(self):
        directory = TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        folder = Path(directory.name)
        self.source = folder / "store-export.json"
        self.translations = folder / "reviewed.json"
        self.output = folder / "store.draft.json"
        self.export = {
            "itemid": "123456",
            "export_metadata": {"version": 1.25, "flags": [True, None]},
            "languages": {
                "english": {SHORT: "Repair the station with {crew}.", ABOUT: f"[h2]Signal Station[/h2]\n{ASSET}"},
                "german": {SHORT: "", ABOUT: "", "app[content][legal]": "© Signal Station"},
                "french": {SHORT: "Réparez la station."},
            },
        }
        self.source.write_text(json.dumps(self.export), encoding="utf-8-sig")

    def run_helper(self, fields, *options):
        self.translations.write_text(json.dumps(fields, ensure_ascii=False), encoding="utf-8")
        return subprocess.run(
            [sys.executable, "-B", str(HELPER), str(self.source), str(self.translations), str(self.output),
             "--target-language", "german", *options],
            capture_output=True, encoding="utf-8", check=False,
        )

    def test_writes_only_selected_fields_and_keeps_import_pending(self):
        fields = {
            "short_description": "Repariere die Station mit {crew}.",
            "about": f"[h2]Signal Station[/h2]\nStelle die Stromversorgung wieder her.\n{ASSET}",
        }
        original = self.source.read_bytes()
        result = self.run_helper(fields, "--short-limit", "90")
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["status"], "draft")
        self.assertEqual(report["steamworks_import"], "pending")
        self.assertEqual(report["fields"]["short_description"]["length_status"], "passed")
        self.assertEqual(report["fields"]["about"]["length_status"], "pending")
        self.assertEqual(report["fields"]["about"]["utf8_bytes"], len(fields["about"].encode("utf-8")))
        expected = copy.deepcopy(self.export)
        expected["languages"]["german"].update({SHORT: fields["short_description"], ABOUT: fields["about"]})
        self.assertEqual(json.loads(self.output.read_text(encoding="utf-8")), expected)
        self.assertEqual(self.source.read_bytes(), original)

    def test_rejects_length_format_and_protected_text_changes_without_writing(self):
        cases = [
            ({"short_description": "Repariere mit {crew}."}, ("--short-limit", "5"), "exceed the supplied limit"),
            ({"short_description": "Repariere\nmit {crew}."}, (), "plain, single-line text"),
            ({"short_description": "[b]Repariere[/b] mit {crew}."}, (), "plain, single-line text"),
            ({"short_description": "<b>Repariere</b> mit {crew}."}, (), "plain, single-line text"),
            ({"short_description": "Repariere die Station."}, (), "protected_tokens"),
            ({"about": f"[h1]Signal Station[/h1]\n{ASSET}"}, (), "BBCode"),
            ({"about": f"[h2]Signal Station[/h2]\n{ASSET.replace('repair.png', 'changed.png')}"}, (), "image or link"),
            ({"other": "Text"}, (), "Use short_description, about, or both"),
        ]
        for fields, options, message in cases:
            with self.subTest(fields=fields):
                result = self.run_helper(fields, *options)
                self.assertEqual(result.returncode, 2, result.stderr)
                self.assertIn(message, result.stderr)
                self.assertFalse(self.output.exists())

    def test_checks_populated_target_and_output_path(self):
        current = "Repariere mit {crew}."
        self.export["languages"]["german"][SHORT] = current
        self.source.write_text(json.dumps(self.export), encoding="utf-8")
        updated = {"short_description": "Repariere die Station mit {crew}."}
        result = self.run_helper(updated)
        self.assertEqual(result.returncode, 2)
        self.assertIn("Target already contains text", result.stderr)
        self.assertFalse(self.output.exists())

        result = self.run_helper({"short_description": current})
        self.assertEqual(result.returncode, 0, result.stderr)
        original_draft = self.output.read_bytes()
        result = self.run_helper(updated, "--replace-existing")
        self.assertEqual(result.returncode, 2)
        self.assertEqual(self.output.read_bytes(), original_draft)

        self.output.unlink()
        result = self.run_helper(updated, "--replace-existing")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(self.output.read_text(encoding="utf-8"))["languages"]["german"][SHORT],
                         updated["short_description"])

    def test_rejects_missing_target_and_duplicate_export_keys(self):
        del self.export["languages"]["german"]
        self.source.write_text(json.dumps(self.export), encoding="utf-8")
        result = self.run_helper({"short_description": "Repariere mit {crew}."})
        self.assertEqual(result.returncode, 2)
        self.assertIn("must already have an object", result.stderr)

        self.source.write_text('{"itemid": "123", "itemid": "456", "languages": {}}', encoding="utf-8")
        result = self.run_helper({"short_description": "Repariere mit {crew}."})
        self.assertEqual(result.returncode, 2)
        self.assertIn("Duplicate JSON key", result.stderr)
        self.assertFalse(self.output.exists())


if __name__ == "__main__":
    unittest.main()
