from datetime import date
from collections import Counter


class SimpleReport:
    def __get_oldest_manufacturing_date(products):
        return min(
            date.fromisoformat(product["data_de_fabricacao"])
            for product in products
        ).isoformat()

    def __get_closest_expiration_date(products):
        return min(
            date.fromisoformat(product["data_de_validade"])
            for product in products
            if date.fromisoformat(product["data_de_validade"]) >= date.today()
        ).isoformat()

    def __get_company_with_bigger_stock(products):
        companies = [product["nome_da_empresa"] for product in products]
        return Counter(companies).most_common(1)[0][0]

    @classmethod
    def generate(cls, products):
        oldest_manufacturing_date = (
            SimpleReport.__get_oldest_manufacturing_date(products)
        )
        closest_expiration_date = SimpleReport.__get_closest_expiration_date(
            products
        )
        company_with_bigger_stock = (
            SimpleReport.__get_company_with_bigger_stock(products)
        )
        return (
            f"Data de fabricação mais antiga: {oldest_manufacturing_date}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            f"Empresa com mais produtos: {company_with_bigger_stock}"
        )
