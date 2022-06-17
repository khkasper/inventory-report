import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    if len(sys.argv) < 3:
        print("Verifique os argumentos", file=sys.stderr)
    else:
        _, path, type = sys.argv
        file = ""
        if path.endswith(".csv"):
            file = InventoryRefactor(CsvImporter)
        if path.endswith(".json"):
            file = InventoryRefactor(JsonImporter)
        if path.endswith(".xml"):
            file = InventoryRefactor(XmlImporter)
        print(file.import_data(path, type), end="")
