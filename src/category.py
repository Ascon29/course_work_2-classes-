from abc import ABC

from src.product import Product, abstractmethod


class BaseCategory(ABC):

    @abstractmethod
    def products(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Category(BaseCategory):
    """Класс для продуктов"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
        else:
            raise TypeError
        Category.product_count += 1

    @property
    def products_list(self):
        return self.__products

    def __str__(self):
        count = 0
        for product in self.products_list:
            count += product.quantity
        return f"{self.name}, количество продуктов: {count} шт."

    def middle_price(self):
        total_price = 0
        total_quantity = 0
        try:
            for product in self.products_list:
                total_price += product.price * product.quantity
                total_quantity += product.quantity
            avg_price = total_price / total_quantity
        except ZeroDivisionError:
            avg_price = 0
        return round(avg_price, 1)
