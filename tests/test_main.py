def test_product(product):
    assert product.name == "Samsung"
    assert product.description == "256Gb"
    assert product.price == 25000
    assert product.quantity == 1


def test_category(category_1, category_2):
    assert category_1.name == "Смартфоны"
    assert category_1.description == "Смартфоны, как средство"
    assert len(category_1.products) == 3

    assert category_2.name == "Телевизоры"
    assert category_2.description == "Телевизоры для просмотра"
    assert len(category_2.products) == 2

    assert category_1.category_count == 2
    assert category_2.category_count == 2

    assert category_1.product_count == 5
    assert category_2.product_count == 5
