import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def check_file_type(cls, file):
        with open(file) as data:
            if file.endswith("csv"):
                return list(csv.DictReader(data))
            elif file.endswith(".json"):
                return json.load(data)
            elif file.endswith(".xml"):
                return xmltodict.parse(data.read())["dataset"]["record"]

    @classmethod
    def import_data(cls, file, type):
        inventory = cls.check_file_type(file)
        if type == "simples":
            return SimpleReport.generate(inventory)
        elif type == "completo":
            return CompleteReport.generate(inventory)


# https://www.geeksforgeeks.org/python-program-to-convert-xml-to-dictionary/ #
