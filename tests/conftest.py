import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product():
    return Product(name="Samsung", description="256Gb", price=25000, quantity=1)


@pytest.fixture
def product_1():
    return {"name": "LG", "description": "4K", "price": 30000, "quantity": 4}


@pytest.fixture
def category_1():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство",
        products=[
            Product(name="Samsung", description="256Gb", price=25000, quantity=1),
            Product(name="Xiaomi", description="512Gb", price=30000, quantity=0),
            Product(name="Iphone", description="256Gb", price=50000, quantity=5),
        ],
    )


@pytest.fixture
def category_2():
    return Category(
        name="Телевизоры",
        description="Телевизоры для просмотра",
        products=[
            Product(name="LG", description="4K", price=30000, quantity=4),
            Product(name="Philips", description="Подсветка", price=60000, quantity=2),
        ],
    )


@pytest.fixture
def product__add__():
    return Product(name="Samsung", description="256Gb", price=25000, quantity=2)


@pytest.fixture
def product2__add__():
    return Product(name="Xiaomi", description="512Gb", price=30000, quantity=5)
