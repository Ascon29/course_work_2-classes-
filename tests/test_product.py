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
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

    product.price = 30000
    assert product.price == 30000


def test__str__(product):
    assert str(product) == "Samsung, 25000 руб. Остаток: 1 шт."


def test__add__(product__add__, product2__add__):
    assert product__add__ + product2__add__ == 200000
