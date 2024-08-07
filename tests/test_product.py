import pytest

from src.product import Product


def test_product(product):
    assert product.name == "Samsung"
    assert product.description == "256Gb"
    assert product.price == 25000
    assert product.quantity == 1


def test_new_product(product_1):
    new = Product.new_product(product_1)
    assert new.name == "LG"
    assert new.description == "4K"
    assert new.price == 30000
    assert new.quantity == 4


def test_price(capsys, product):
    product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == (
        "Product(Samsung, 256Gb, 25000, 1)\n" "Цена не должна быть нулевая или отрицательная"
    )

    product.price = 30000
    assert product.price == 30000


def test__str__(product):
    assert str(product) == "Samsung, 25000 руб. Остаток: 1 шт."


def test__add__(product__add__, product2__add__, product_not_class_object):
    assert product__add__ + product2__add__ == 200000

    with pytest.raises(TypeError):
        assert product__add__ + product_not_class_object


def test_smartphone(smartphone_1):
    assert smartphone_1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_1.price == 180000.0
    assert smartphone_1.quantity == 5
    assert smartphone_1.efficiency == 95.5
    assert smartphone_1.model == "S23 Ultra"
    assert smartphone_1.memory == 256
    assert smartphone_1.color == "Серый"


def test_lawngrass(lawngrass_1):
    assert lawngrass_1.name == "Газонная трава"
    assert lawngrass_1.description == "Элитная трава для газона"
    assert lawngrass_1.price == 500.0
    assert lawngrass_1.quantity == 20
    assert lawngrass_1.country == "Россия"
    assert lawngrass_1.germination_period == "7 дней"
    assert lawngrass_1.color == "Зеленый"


def test_add_smartphone(smartphone_1, smartphone_2):
    assert smartphone_1 + smartphone_2 == 1334000.0


def test_add_lawngrass(lawngrass_1, lawngrass_2):
    assert lawngrass_1 + lawngrass_2 == 16750.0


def test__add__not_class(smartphone_1, lawngrass_1):
    with pytest.raises(TypeError):
        assert smartphone_1 + lawngrass_1


def test_mixin_product(capsys, product):
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Samsung, 256Gb, 25000, 1)"


def test_mixin_smartphone(capsys, smartphone_1):
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"


def test_mixin_lawngrass(capsys, lawngrass_1):
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"
