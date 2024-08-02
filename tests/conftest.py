import pytest

from src.category import Category
from src.product import LawnGrass, Product, Smartphone


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


@pytest.fixture
def smartphone_1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def smartphone_2():
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")


@pytest.fixture
def lawngrass_1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawngrass_2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def product_not_class_object():
    return "Not a product"
