from src.category import BaseCategory
from src.product import Product


class Order(BaseCategory):

    product: Product
    quantity: int

    def __init__(self, product: Product, quantity: int):
        self.__product = product
        self.__quantity = quantity
        self.__total_price = 0

    @property
    def products(self):
        return self.__product

    @property
    def quantity(self):
        return self.__quantity

    @property
    def total_price(self):
        self.__total_price = self.products.price * self.quantity
        return self.__total_price

    def __str__(self):
        return f"Куплено {self.quantity} {self.products.name}. Итоговая стоимость {self.__total_price}"


if __name__ == "__main__":
    product1 = Product("Samsung", "s10", 100, 90)
    order1 = Order(product1, 10)
    print(order1.products)
    print(order1.quantity)
    print(order1.total_price)
    print(str(order1))
