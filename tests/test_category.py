import pytest


def test_category(category_1, category_2):
    assert category_1.name == "Смартфоны"
    assert category_1.description == "Смартфоны, как средство"
    assert len(category_1.products_list) == 3

    assert category_2.name == "Телевизоры"
    assert category_2.description == "Телевизоры для просмотра"
    assert len(category_2.products_list) == 2

    assert category_1.category_count == 2
    assert category_2.category_count == 2

    assert category_1.product_count == 5
    assert category_2.product_count == 5


def test_products_list_property(category_1):
    assert category_1.products == (
        "Samsung, 25000 руб. Остаток: 1 шт.\n"
        "Xiaomi, 30000 руб. Остаток: 0 шт.\n"
        "Iphone, 50000 руб. Остаток: 5 шт.\n"
    )


def test_add_product(category_1, product):
    assert len(category_1.products_list) == 3
    category_1.add_product(product)
    assert len(category_1.products_list) == 4


def test__str__(category_1):
    assert str(category_1) == "Смартфоны, количество продуктов: 6 шт."


def test_add_pruduct_not_class(category_1, product_not_class_object):
    with pytest.raises(TypeError):
        category_1.add_product(product_not_class_object)
