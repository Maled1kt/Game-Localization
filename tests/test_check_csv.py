import csv
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


CHECKER = Path(__file__).resolve().parents[1] / "game-localization" / "scripts" / "check_csv.py"


class CheckCsvTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.source = Path(directory.name) / "source.csv"
        self.target = Path(directory.name) / "target.csv"

    def write_csv(self, path, headers, rows, delimiter=","):
        with path.open("w", encoding="utf-8-sig", newline="") as stream:
            writer = csv.writer(stream, delimiter=delimiter)
            writer.writerow(headers)
            writer.writerows(rows)

    def check(self, *options):
        result = subprocess.run(
            [sys.executable, str(CHECKER), str(self.source), str(self.target),
             "--id-column", "ID", "--source-column", "EN", "--target-column", "RU", *options],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertTrue(result.stdout, result.stderr)
        return result.returncode, json.loads(result.stdout)

    def test_checks_quoted_csv_and_matches_ids_independently_of_row_order(self):
        self.write_csv(self.source, ["ID", "EN"], [
            ("TUT_014", 'Hold {interact}; open <b>{0}</b>\n"Confirmed"'),
            ("STAT_005", "%1$s has %2$d%%"),
        ], delimiter=";")
        self.write_csv(self.target, ["ID", "RU"], [
            ("STAT_005", "%2$d%% у %1$s"),
            ("TUT_014", 'Удерживайте {interact}; откройте <b>{0}</b>\n"Подтверждено"'),
        ], delimiter=";")

        code, report = self.check("--delimiter", "semicolon")

        self.assertEqual(code, 0)
        self.assertEqual(report, {
            "status": "passed", "source_ids": 2, "target_ids": 2, "checked_rows": 2, "issues": [],
        })

    def test_reports_missing_and_extra_ids_duplicate_rows_and_changed_tokens(self):
        self.write_csv(self.source, ["ID", "EN"], [
            ("TUT_014", "Hold {interact} to open {airlock}. Release {interact} to cancel."),
            ("MENU_001", "Continue"),
            ("MENU_002", "Quit"),
            ("MENU_003", "Back"),
        ])
        self.write_csv(self.target, ["ID", "RU"], [
            ("TUT_014", "Удерживайте {interact}, чтобы открыть {airlock}<b>.</b>"),
            ("MENU_002", "Выход"),
            ("MENU_002", "Выйти"),
            ("MENU_003", " "),
            ("MENU_004", "Играть"),
        ])

        code, report = self.check()

        self.assertEqual(code, 1)
        self.assertEqual(report["status"], "failed")
        issues = {issue["code"]: issue for issue in report["issues"]}
        self.assertEqual(issues["missing_id"]["id"], "MENU_001")
        self.assertEqual(issues["unexpected_id"]["id"], "MENU_004")
        self.assertEqual(issues["duplicate_id"]["id"], "MENU_002")
        self.assertEqual(issues["empty_translation"]["id"], "MENU_003")
        self.assertEqual(issues["protected_tokens"], {
            "id": "TUT_014", "code": "protected_tokens",
            "missing": {"{interact}": 1}, "unexpected": {"<b>": 1, "</b>": 1},
        })

    def test_flags_reordered_printf_arguments_and_tags(self):
        self.write_csv(self.source, ["ID", "EN"], [("HUD", '<b>%s</b> <color="#fff">%d</color>')])
        self.write_csv(self.target, ["ID", "RU"], [("HUD", '<color="#fff">%d</color> <b>%s</b>')])

        code, report = self.check()

        self.assertEqual(code, 1)
        self.assertEqual({issue["code"] for issue in report["issues"]}, {"tag_order", "printf_order"})

    def test_distinguishes_character_and_byte_limits(self):
        self.write_csv(self.source, ["ID", "EN", "MAX"], [("UI", "Go", "2"), ("DIA", "Hello", "")])
        self.write_csv(self.target, ["ID", "RU"], [("UI", "Да"), ("DIA", "Привет")])

        character_code, _ = self.check("--limit-column", "MAX", "--limit-unit", "characters")
        byte_code, report = self.check("--limit-column", "MAX", "--limit-unit", "utf8-bytes")

        self.assertEqual(character_code, 0)
        self.assertEqual(byte_code, 1)
        self.assertEqual(report["issues"], [
            {"id": "UI", "code": "length_limit", "unit": "utf8-bytes", "limit": 2, "actual": 4},
        ])

    def test_rejects_unreadable_or_malformed_input(self):
        self.write_csv(self.source, ["ID", "EN"], [("UI", "Go")])
        for invalid_target in (b'ID,RU\nUI,"unfinished', b"ID,RU\nUI,\xff", b"ID,RU\nUI,Go,extra"):
            with self.subTest(invalid_target=invalid_target):
                self.target.write_bytes(invalid_target)

                code, report = self.check()

                self.assertEqual(code, 2)
                self.assertEqual(report["checked_rows"], 0)
                self.assertEqual(report["issues"][0]["code"], "invalid_csv")


if __name__ == "__main__":
    unittest.main()
