from src.category import Category
from src.product import Product


class ProductIterator:
    """Вспомогательный класс для итерации по продуктам в категории"""

    def __init__(self, category_obj):
        self.category_obj = category_obj
        self.count = 0

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        if self.count < len(self.category_obj.products_list):
            product = self.category_obj.products_list[self.count]
            self.count += 1
            return product
        else:
            raise StopIteration


if __name__ == "__main__":

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    x = ProductIterator(category1)

    for i in x:
        print(i)
