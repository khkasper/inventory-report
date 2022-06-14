import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file):
        if not file.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        with open(file) as data:
            return list(csv.DictReader(data))
