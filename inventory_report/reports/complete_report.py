from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def __get_company_products_quantity(products):
        report = ""
        products_quantity = Counter(
            company["nome_da_empresa"] for company in products
        )
        for company, count in products_quantity.items():
            report += f"- {company}: {count}\n"
        return report

    @classmethod
    def generate(cls, products):
        return (
            super().generate(products)
            + "\nProdutos estocados por empresa:\n"
            + CompleteReport.__get_company_products_quantity(products)
        )
