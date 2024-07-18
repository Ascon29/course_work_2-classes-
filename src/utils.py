import json
import os

from src.main import Category, Product


def read_json(filename):
    """
    функция считывает json файл
    возвращает список категорий продуктов
    :param filename: json файл
    :return: список словарей
    """
    full_path = os.path.abspath(filename)
    with open(full_path, "r", encoding="utf-8") as file:
        result_data = json.load(file)
    return result_data


def create_objects_from_json(data):
    """
    функция подгружает данные про категориям и товарам из файла json. создает обьекты классов
    :param data: список словарей
    :return: список с обьектами классов
    """
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories


if __name__ == "__main__":
    x = read_json("../data/products.json")
    users = create_objects_from_json(x)
    print(users[0].name)
    print(users[0].products)
