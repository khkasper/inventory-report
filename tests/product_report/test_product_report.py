from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "Nicotine Polacrilex",
        "Target Corporation",
        "2020-02-18",
        "2022-09-17",
        "CR25 1551 4467 2549 4402 1",
        "instrucao 1",
    )
    result = (
        f"O produto {product.nome_do_produto} "
        f"fabricado em {product.data_de_fabricacao} "
        f"por {product.nome_da_empresa} com validade "
        f"até {product.data_de_validade} "
        f"precisa ser armazenado {product.instrucoes_de_armazenamento}."
    )
    assert str(product) == result
