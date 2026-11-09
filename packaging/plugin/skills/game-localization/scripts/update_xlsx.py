"""Write reviewed translations to one column of a new .xlsx copy."""

import argparse
from copy import copy
import csv
import json
from pathlib import Path
import posixpath
import re
import shutil
import sys
from tempfile import TemporaryFile
from xml.dom import Node, minidom
from xml.parsers.expat import ExpatError
from zipfile import BadZipFile, ZipFile


MAIN = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
OFFICE_REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PACKAGE_REL = "http://schemas.openxmlformats.org/package/2006/relationships"
CONTENT_TYPES = "http://schemas.openxmlformats.org/package/2006/content-types"
WORKBOOK_TYPE = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"
XML = "http://www.w3.org/XML/1998/namespace"
CELL = re.compile(r"([A-Z]{1,3})([1-9][0-9]{0,6})")
ESCAPE = re.compile(r"_x[0-9a-fA-F]{4}_")


def children(node, name=None, namespace=MAIN):
    return [
        child for child in node.childNodes
        if child.nodeType == Node.ELEMENT_NODE
        and (name is None or (child.localName, child.namespaceURI) == (name, namespace))
    ]


def one(node, name):
    matches = children(node, name)
    if len(matches) > 1:
        raise ValueError(f"Unexpected repeated {name} element.")
    return matches[0] if matches else None


def element(parent, name):
    prefix = f"{parent.prefix}:" if parent.prefix else ""
    return parent.ownerDocument.createElementNS(MAIN, prefix + name)


def parse(data, name, namespace=MAIN):
    doc = minidom.parseString(data)
    root = doc.documentElement
    if doc.doctype or (root.localName, root.namespaceURI) != (name, namespace):
        raise ValueError(f"Unsupported {name} XML.")
    return root


def text(node):
    if node is None:
        return ""
    return "".join(
        child.data for child in node.childNodes
        if child.nodeType in (Node.TEXT_NODE, Node.CDATA_SECTION_NODE)
    )


def plain_string(node):
    nodes = children(node)
    if len(nodes) != 1 or nodes[0] is not one(node, "t") or children(nodes[0]):
        raise ValueError("Rich text in an ID, header, or target cell is unsupported.")
    return text(nodes[0])


def decode_string(value):
    decoded = ESCAPE.sub(lambda match: chr(int(match[0][2:6], 16)), value)
    return decoded.encode("utf-16-le", "surrogatepass").decode("utf-16-le")


def add_text(parent, value):
    node = element(parent, "t")
    node.setAttributeNS(XML, "xml:space", "preserve")
    encoded = ESCAPE.sub(lambda match: "_x005F_" + match[0][1:], value)
    node.appendChild(parent.ownerDocument.createTextNode(encoded.replace("\r", "_x000D_")))
    parent.appendChild(node)


def coordinates(address):
    match = CELL.fullmatch(address)
    if not match:
        raise ValueError(f"Unsupported cell address {address!r}.")
    column = 0
    for letter in match[1]:
        column = column * 26 + ord(letter) - ord("A") + 1
    row = int(match[2])
    if column > 16384 or row > 1048576:
        raise ValueError(f"Cell address {address!r} exceeds the worksheet limits.")
    return column, row


def read_translations(path):
    translations = {}
    with path.open(encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file, strict=True)
        if next(reader, None) != ["ID", "TRANSLATION"]:
            raise ValueError("The translation CSV must have the headers ID,TRANSLATION.")
        for record in reader:
            if len(record) != 2:
                raise ValueError(f"Expected two fields on CSV line {reader.line_num}.")
            id_, value = record
            if not id_.strip() or not value.strip():
                raise ValueError(f"Blank ID or translation on CSV line {reader.line_num}.")
            if id_ in translations:
                raise ValueError(f"Duplicate CSV ID {id_!r}.")
            if (len(value.encode("utf-16-le")) // 2 > 32767 or value.count("\n") > 253
                    or re.search(r"[^\t\n\r\x20-\uD7FF\uE000-\uFFFD\U00010000-\U0010FFFF]", value)):
                raise ValueError(f"Translation for {id_!r} exceeds Excel limits or contains invalid characters.")
            translations[id_] = value
    if not translations:
        raise ValueError("The translation CSV has no rows.")
    return translations


def part_path(relationship):
    target = relationship.getAttribute("Target")
    if (not target or "\\" in target
            or relationship.getAttribute("TargetMode") not in ("", "Internal")):
        raise ValueError("Unsupported workbook relationship target.")
    return posixpath.normpath(target.lstrip("/") if target.startswith("/") else f"xl/{target}")


def workbook_parts(archive, sheet_name):
    names = archive.namelist()
    if (len(names) != len(set(names))
            or any(name.lower().startswith("_xmlsignatures/") for name in names)):
        raise ValueError("Signed workbooks and archives with duplicate entries are unsupported.")
    types = parse(archive.read("[Content_Types].xml"), "Types", CONTENT_TYPES)
    workbook_types = [
        node.getAttribute("ContentType") for node in children(types, "Override", CONTENT_TYPES)
        if node.getAttribute("PartName") == "/xl/workbook.xml"
    ]
    if workbook_types != [WORKBOOK_TYPE]:
        raise ValueError("The archive does not contain a standard .xlsx workbook.")
    workbook = parse(archive.read("xl/workbook.xml"), "workbook")
    rels = parse(archive.read("xl/_rels/workbook.xml.rels"), "Relationships", PACKAGE_REL)
    relationships = children(rels, "Relationship", PACKAGE_REL)
    sheets = [
        sheet for sheet in children(one(workbook, "sheets"), "sheet")
        if sheet.getAttribute("name") == sheet_name
    ]
    if len(sheets) != 1:
        raise ValueError(f"Expected exactly one sheet named {sheet_name!r}.")
    sheet_id = sheets[0].getAttributeNS(OFFICE_REL, "id")
    matches = [
        rel for rel in relationships
        if rel.getAttribute("Id") == sheet_id and rel.getAttribute("Type") == f"{OFFICE_REL}/worksheet"
    ]
    if not sheet_id or len(matches) != 1:
        raise ValueError("The selected sheet is not a supported worksheet.")
    strings = [rel for rel in relationships if rel.getAttribute("Type") == f"{OFFICE_REL}/sharedStrings"]
    if len(strings) > 1:
        raise ValueError("The workbook has multiple shared string tables.")
    return part_path(matches[0]), part_path(strings[0]) if strings else None


def cell_value(cell, strings, *, allow_number=False):
    if one(cell, "f") is not None:
        raise ValueError(f"Cell {cell.getAttribute('r')} contains a formula.")
    kind = cell.getAttribute("t")
    value = text(one(cell, "v"))
    if kind == "s":
        if not re.fullmatch(r"[0-9]+", value) or int(value) >= len(strings):
            raise ValueError(f"Invalid shared string index in {cell.getAttribute('r')}.")
        return decode_string(plain_string(strings[int(value)]))
    if kind == "inlineStr":
        inline = one(cell, "is")
        return decode_string(plain_string(inline)) if inline is not None else ""
    if kind == "str":
        return decode_string(value)
    if kind in ("", "n") and (not value or allow_number):
        return value
    raise ValueError(f"Cell {cell.getAttribute('r')} must contain plain text or a literal ID.")


def worksheet_rows(sheet):
    data = one(sheet, "sheetData")
    if data is None:
        raise ValueError("The selected worksheet has no sheet data.")
    rows = {}
    for row in children(data, "row"):
        index = int(row.getAttribute("r"))
        if index in rows or not 1 <= index <= 1048576:
            raise ValueError(f"Invalid or repeated worksheet row {index}.")
        cells = {}
        for cell in children(row, "c"):
            column, actual_row = coordinates(cell.getAttribute("r"))
            if column in cells or index != actual_row:
                raise ValueError(f"Invalid or repeated cell address {cell.getAttribute('r')!r}.")
            cells[column] = cell
        rows[index] = row, cells
    return rows


def header_column(cells, strings, name):
    matches = []
    for column, cell in cells.items():
        # Formula results and non-text cells cannot select a column.
        if cell.getAttribute("t") not in ("s", "inlineStr", "str") or one(cell, "f") is not None:
            continue
        if cell_value(cell, strings) == name:
            matches.append(column)
    if len(matches) != 1:
        raise ValueError(f"Expected exactly one plain-text header {name!r}.")
    return matches[0]


def edit_plan(rows, strings, translations, header_row, id_header, target_header):
    _, headers = rows.get(header_row, (None, {}))
    id_column = header_column(headers, strings, id_header)
    target_column = header_column(headers, strings, target_header)
    column_letters = CELL.fullmatch(headers[target_column].getAttribute("r"))[1]
    ids = set()
    plan = {}
    for index, (row, cells) in rows.items():
        if index <= header_row or id_column not in cells:
            continue
        id_ = cell_value(cells[id_column], strings, allow_number=True)
        if not id_:
            continue
        if id_ in ids:
            raise ValueError(f"Duplicate worksheet ID {id_!r} on row {index}.")
        ids.add(id_)
        if id_ in translations:
            plan[f"{column_letters}{index}"] = row, cells.get(target_column), translations[id_]
    unknown = translations.keys() - ids
    if unknown:
        raise ValueError(f"CSV IDs missing from the worksheet: {', '.join(sorted(unknown))}.")
    return plan


def check_ranges(sheet, plan):
    if one(sheet, "sheetProtection") is not None:
        raise ValueError("The selected worksheet is protected.")
    addresses = {address: coordinates(address) for address in plan}
    ranges = list(sheet.getElementsByTagNameNS(MAIN, "mergeCell"))
    ranges.extend(
        formula for formula in sheet.getElementsByTagNameNS(MAIN, "f") if formula.hasAttribute("ref")
    )
    for item in ranges:
        first, _, last = item.getAttribute("ref").partition(":")
        left, top = coordinates(first)
        right, bottom = coordinates(last or first)
        for address, (column, row) in addresses.items():
            if left <= column <= right and top <= row <= bottom:
                raise ValueError(f"Target {address} intersects a merged cell or formula range.")


def write_cell(row, cell, address, value, table, strings, new_strings):
    kind = ""
    if cell is not None:
        kind = cell.getAttribute("t")
        content = children(cell)
        if (cell.hasAttribute("cm") or cell.hasAttribute("vm") or cell.hasAttribute("ph")
                or any(node.namespaceURI != MAIN or node.localName not in ("v", "is") for node in content)
                or (kind in ("", "n") and text(one(cell, "v")))):
            raise ValueError(f"Target {address} is not an editable blank or plain-text cell.")
        cell_value(cell, strings)
    else:
        cell = element(row, "c")
        cell.setAttribute("r", address)
        column, _ = coordinates(address)
        for sibling in children(row):
            if (sibling.localName != "c" or sibling.namespaceURI != MAIN
                    or coordinates(sibling.getAttribute("r"))[0] > column):
                row.insertBefore(cell, sibling)
                break
        else:
            row.appendChild(cell)

    for child in list(cell.childNodes):
        cell.removeChild(child)
    if kind == "s":
        if value not in new_strings:
            new_strings[value] = len(strings)
            item = element(table, "si")
            add_text(item, value)
            table.insertBefore(item, one(table, "extLst"))
            strings.append(item)
        index = element(cell, "v")
        index.appendChild(cell.ownerDocument.createTextNode(str(new_strings[value])))
        cell.appendChild(index)
    else:
        cell.setAttribute("t", "inlineStr")
        inline = element(cell, "is")
        add_text(inline, value)
        cell.appendChild(inline)


def masked_sheet(sheet, addresses):
    """Remove only the expected target cells from a fresh parsed worksheet."""
    for cell in list(sheet.getElementsByTagNameNS(MAIN, "c")):
        if cell.getAttribute("r") in addresses:
            cell.parentNode.removeChild(cell)
    return sheet.ownerDocument.toxml()


def shared_string_indices(strings):
    indices = {}
    for index, item in enumerate(strings):
        if len(children(item)) == 1 and one(item, "t") is not None:
            indices[decode_string(plain_string(item))] = index
    return indices


def update_workbook(source, translation_csv, output, sheet_name, id_header, target_header, header_row=1):
    if source.suffix.lower() != ".xlsx" or output.suffix.lower() != ".xlsx":
        raise ValueError("The source and output must be .xlsx files.")
    if output.exists():
        raise ValueError("Choose a new output path. The existing file was kept.")
    if (not 1 <= header_row <= 1048576 or not id_header.strip()
            or not target_header.strip() or id_header == target_header):
        raise ValueError("Specify a valid header row and two different, nonblank column headers.")
    translations = read_translations(translation_csv)

    with ZipFile(source) as original, TemporaryFile() as temporary:
        sheet_path, table_path = workbook_parts(original, sheet_name)
        sheet_data = original.read(sheet_path)
        sheet = parse(sheet_data, "worksheet")
        table = parse(original.read(table_path), "sst") if table_path else None
        strings = children(table, "si") if table is not None else []
        original_string_count = len(strings)
        plan = edit_plan(worksheet_rows(sheet), strings, translations, header_row, id_header, target_header)
        check_ranges(sheet, plan)
        new_strings = shared_string_indices(strings)
        styles = {address: cell.getAttribute("s") for address, (_, cell, _) in plan.items() if cell is not None}
        for address, (row, cell, value) in plan.items():
            write_cell(row, cell, address, value, table, strings, new_strings)
        replacements = {sheet_path: sheet.ownerDocument.toxml(encoding="UTF-8")}
        if len(strings) != original_string_count:
            if table.hasAttribute("uniqueCount"):
                table.setAttribute("uniqueCount", str(len(strings)))
            replacements[table_path] = table.ownerDocument.toxml(encoding="UTF-8")

        with ZipFile(temporary, "w") as updated:
            updated.comment = original.comment
            for entry in original.infolist():
                name = entry.filename
                content = replacements[name] if name in replacements else original.read(entry)
                updated.writestr(copy(entry), content)

        with ZipFile(temporary) as updated:
            if updated.namelist() != original.namelist() or updated.testzip() is not None:
                raise ValueError("Could not verify the output workbook archive.")
            for name in updated.namelist():
                expected = replacements[name] if name in replacements else original.read(name)
                if updated.read(name) != expected:
                    raise ValueError(f"Could not verify workbook part {name!r}.")
            saved = parse(updated.read(sheet_path), "worksheet")
            saved_table = children(parse(updated.read(table_path), "sst"), "si") if table_path else []
            if table_path in replacements:
                prior_table = parse(original.read(table_path), "sst")
                prior_strings = children(prior_table, "si")
                if [item.toxml() for item in saved_table[:original_string_count]] != [
                    item.toxml() for item in prior_strings
                ]:
                    raise ValueError("Existing shared strings changed.")
            saved_cells = {cell.getAttribute("r"): cell for cell in saved.getElementsByTagNameNS(MAIN, "c")}
            for address, (_, _, value) in plan.items():
                saved_cell = saved_cells[address]
                if cell_value(saved_cell, saved_table) != value or saved_cell.getAttribute("s") != styles.get(address, ""):
                    raise ValueError(f"Translation or style at {address} failed the read-back check.")
            if masked_sheet(saved, plan) != masked_sheet(parse(sheet_data, "worksheet"), plan):
                raise ValueError("The output worksheet changed outside the requested cells.")

        temporary.seek(0)
        created = output.open("xb")
        try:
            with created:
                shutil.copyfileobj(temporary, created)
        except BaseException:
            output.unlink()
            raise
    return {"status": "passed", "sheet": sheet_name, "updated_cells": list(plan)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("translation_csv", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--sheet", required=True)
    parser.add_argument("--id-column", required=True)
    parser.add_argument("--target-column", required=True)
    parser.add_argument("--header-row", type=int, default=1)
    args = parser.parse_args()
    try:
        report = update_workbook(args.source, args.translation_csv, args.output, args.sheet,
                                 args.id_column, args.target_column, args.header_row)
    except (BadZipFile, csv.Error, ExpatError, KeyError, OSError, RuntimeError, ValueError) as error:
        parser.exit(2, f"Workbook update failed: {error}\n")
    print(json.dumps(report, ensure_ascii=True))


if __name__ == "__main__":
    main()
