from abc import ABC, abstractmethod


class MixinLog:
    """Класс-миксин, который печататает в консоль информацию о том,
    от какого класса и с какими параметрами был создан объект"""

    def __init__(self):
        self.__repr__()

    def __repr__(self):
        print(f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})")


class BaseProduct(ABC):
    """Базовый абстрактный родительский класс для класса продуктов"""

    @classmethod
    @abstractmethod
    def new_product(cls, kwargs):
        pass


class Product(MixinLog, BaseProduct):
    """класс для категорий продуктов"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    @classmethod
    def new_product(cls, kwargs):
        return cls(**kwargs)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            answer = input("Вы действительно хотите снизить цену? y/n\n").lower()
            if answer == "y":
                self.__price = new_price
        elif new_price > self.__price:
            self.__price = new_price

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return (self.price * self.quantity) + (other.price * other.quantity)
        else:
            raise TypeError


class Smartphone(Product):
    """Класс для категорий смартфонов"""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для категорий травы"""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


if __name__ == "__main__":
    y = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    print(y)
    x = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")
    print(x)
    z = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    print(z)

    print(Product.__mro__)
