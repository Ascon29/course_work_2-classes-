import pytest

from src.iter_class import ProductIterator


def test_product_iterator(category_1):
    iterator = ProductIterator(category_1)
    assert str(next(iterator)) == "Samsung, 25000 руб. Остаток: 1 шт."
    assert str(next(iterator)) == "Xiaomi, 30000 руб. Остаток: 2 шт."
    assert str(next(iterator)) == "Iphone, 50000 руб. Остаток: 5 шт."
    with pytest.raises(StopIteration):
        next(iterator)
