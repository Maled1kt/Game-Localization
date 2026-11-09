import csv
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest
from xml.etree import ElementTree as ET
from zipfile import ZIP_DEFLATED, ZipFile


UPDATER = Path(__file__).resolve().parents[1] / "game-localization" / "scripts" / "update_xlsx.py"
MAIN = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS = {"m": MAIN}


def workbook_fixture(path, *, target=None, extra="", second_id="MENU_002"):
    target = '<c r="C2" s="1" t="s"><v>4</v></c>' if target is None else target
    with ZipFile(path, "w", compression=ZIP_DEFLATED) as archive:
        archive.writestr("[Content_Types].xml", """<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
<Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
<Override PartName="/xl/worksheets/sheet2.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
<Override PartName="/xl/sharedStrings.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sharedStrings+xml"/>
<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>
</Types>""")
        package_rel = "http://schemas.openxmlformats.org/package/2006/relationships"
        archive.writestr("_rels/.rels", f"""<Relationships xmlns="{package_rel}">
<Relationship Id="rId1" Type="{REL}/officeDocument" Target="xl/workbook.xml"/>
</Relationships>""")
        archive.writestr("xl/workbook.xml", f"""<workbook xmlns="{MAIN}" xmlns:r="{REL}">
<sheets><sheet name="Strings" sheetId="1" r:id="rId1"/><sheet name="Notes" sheetId="2" r:id="rId2"/></sheets>
</workbook>""")
        archive.writestr("xl/_rels/workbook.xml.rels", f"""<Relationships xmlns="{package_rel}">
<Relationship Id="rId1" Type="{REL}/worksheet" Target="worksheets/sheet1.xml"/>
<Relationship Id="rId2" Type="{REL}/worksheet" Target="/xl/worksheets/sheet2.xml"/>
<Relationship Id="rId3" Type="{REL}/sharedStrings" Target="sharedStrings.xml"/>
<Relationship Id="rId4" Type="{REL}/styles" Target="styles.xml"/>
</Relationships>""")
        archive.writestr("xl/sharedStrings.xml", f"""<sst xmlns="{MAIN}" count="{6 if 't="s"' in target else 5}" uniqueCount="5">
<si><t>ID</t></si><si><t>ENGLISH</t></si><si><t>GERMAN</t></si>
<si><t>MENU_001</t></si><si><t>Shared old text</t></si>
</sst>""")
        archive.writestr("xl/styles.xml", f"""<styleSheet xmlns="{MAIN}">
<fonts count="1"><font><sz val="11"/><name val="Calibri"/></font></fonts>
<fills count="2"><fill><patternFill patternType="none"/></fill><fill><patternFill patternType="gray125"/></fill></fills>
<borders count="1"><border><left/><right/><top/><bottom/><diagonal/></border></borders>
<cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>
<cellXfs count="2"><xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/>
<xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0" applyAlignment="1"><alignment wrapText="1"/></xf></cellXfs>
<cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles>
</styleSheet>""")
        archive.writestr("xl/worksheets/sheet1.xml", f"""<worksheet xmlns="{MAIN}">
<cols><col min="3" max="3" width="28" customWidth="1"/></cols>
<sheetData>
<row r="1"><c r="A1" t="s"><v>0</v></c><c r="B1" t="s"><v>1</v></c><c r="C1" t="s"><v>2</v></c></row>
<row r="2"><c r="A2" t="s"><v>3</v></c><c r="B2" t="inlineStr"><is><t>Play {{name}}</t></is></c>
{target}<c r="D2"><f>LEN(B2)</f><v>11</v></c></row>
<row r="3"><c r="A3" t="inlineStr"><is><t>{second_id}</t></is></c>
<c r="B3" t="inlineStr"><is><t>Settings</t></is></c><c r="D3"><v>2</v></c></row>
</sheetData>
{extra}
</worksheet>""")
        archive.writestr("xl/worksheets/sheet2.xml", f"""<worksheet xmlns="{MAIN}">
<sheetData><row r="1"><c r="A1" t="s"><v>4</v></c></row></sheetData>
</worksheet>""")


class UpdateXlsxTests(unittest.TestCase):
    def setUp(self):
        directory = TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.source = Path(directory.name) / "source.xlsx"
        self.translations = Path(directory.name) / "translations.csv"
        self.output = Path(directory.name) / "output.xlsx"

    def run_updater(self, rows):
        with self.translations.open("w", encoding="utf-8-sig", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(("ID", "TRANSLATION"))
            writer.writerows(rows)
        return subprocess.run(
            [sys.executable, str(UPDATER), str(self.source), str(self.translations), str(self.output),
             "--sheet", "Strings", "--id-column", "ID", "--target-column", "GERMAN"],
            capture_output=True, encoding="utf-8", check=False,
        )

    def test_updates_existing_and_missing_cells_by_id_and_preserves_workbook_parts(self):
        workbook_fixture(self.source)
        original_bytes = self.source.read_bytes()
        result = self.run_updater([("MENU_002", "=Einstellungen"), ("MENU_001", " Spielen {name} \n")])
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["updated_cells"], ["C2", "C3"])
        self.assertEqual(self.source.read_bytes(), original_bytes)

        with ZipFile(self.source) as before, ZipFile(self.output) as after:
            self.assertEqual(before.namelist(), after.namelist())
            for name in before.namelist():
                if name not in ("xl/worksheets/sheet1.xml", "xl/sharedStrings.xml"):
                    self.assertEqual(before.read(name), after.read(name), name)
            sheet = ET.fromstring(after.read("xl/worksheets/sheet1.xml"))
            cells = {cell.attrib["r"]: cell for cell in sheet.findall(".//m:c", NS)}
            self.assertEqual(list(cells)[-2:], ["C3", "D3"])
            self.assertEqual(cells["C2"].attrib["s"], "1")
            self.assertEqual(cells["D2"].findtext("m:f", namespaces=NS), "LEN(B2)")
            self.assertEqual(cells["C3"].attrib["t"], "inlineStr")
            self.assertEqual(cells["C3"].findtext("m:is/m:t", namespaces=NS), "=Einstellungen")
            table = ET.fromstring(after.read("xl/sharedStrings.xml"))
            values = [item.findtext("m:t", namespaces=NS) for item in table]
            self.assertEqual(table.attrib, {"count": "6", "uniqueCount": "6"})
            self.assertEqual(values[4], "Shared old text")
            self.assertEqual(values[int(cells["C2"].findtext("m:v", namespaces=NS))], " Spielen {name} \n")

    def test_inline_write_keeps_shared_strings_and_escapes_excel_text(self):
        workbook_fixture(self.source, target='<c r="C2" s="1" t="inlineStr"><is><t>Old</t></is></c>')
        result = self.run_updater([("MENU_001", "Wörtlich _x000D_\rZeile")])
        self.assertEqual(result.returncode, 0, result.stderr)
        with ZipFile(self.source) as before, ZipFile(self.output) as after:
            self.assertEqual(before.read("xl/sharedStrings.xml"), after.read("xl/sharedStrings.xml"))
            sheet = ET.fromstring(after.read("xl/worksheets/sheet1.xml"))
            target = sheet.find(".//m:c[@r='C2']", NS)
            self.assertEqual(target.findtext("m:is/m:t", namespaces=NS), "Wörtlich _x005F_x000D__x000D_Zeile")

    def test_preflight_rejects_unsafe_targets_and_ambiguous_ids(self):
        cases = [
            ({"target": '<c r="C2"><f>1+1</f><v>2</v></c>'}, [("MENU_001", "Spielen")], "C2"),
            ({"target": '<c r="C2"><v>2</v></c>'}, [("MENU_001", "Spielen")], "C2"),
            ({"extra": '<mergeCells count="1"><mergeCell ref="C2:C3"/></mergeCells>'},
             [("MENU_002", "Optionen")], "intersects"),
            ({"target": '<c r="C2"><f t="array" ref="C2:C3">1+1</f><v>2</v></c>'},
             [("MENU_002", "Optionen")], "intersects"),
            ({"extra": '<sheetProtection sheet="1"/>'}, [("MENU_001", "Spielen")], "protected"),
            ({"second_id": "MENU_001"}, [("MENU_001", "Spielen")], "Duplicate worksheet ID"),
            ({}, [("MENU_001", "Spielen"), ("MENU_001", "Neu")], "Duplicate CSV ID"),
            ({}, [("MISSING", "Fehlt")], "missing from the worksheet"),
        ]
        for fixture, rows, message in cases:
            with self.subTest(fixture=fixture, rows=rows):
                workbook_fixture(self.source, **fixture)
                original = self.source.read_bytes()
                result = self.run_updater(rows)
                self.assertEqual(result.returncode, 2, result.stderr)
                self.assertIn(message, result.stderr)
                self.assertFalse(self.output.exists())
                self.assertEqual(self.source.read_bytes(), original)

    def test_keeps_an_existing_output(self):
        workbook_fixture(self.source)
        self.output.write_bytes(b"existing")
        result = self.run_updater([("MENU_001", "Spielen")])
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertEqual(self.output.read_bytes(), b"existing")


if __name__ == "__main__":
    unittest.main()
