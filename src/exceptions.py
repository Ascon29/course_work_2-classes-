class ZeroProductQuantity(Exception):
    """ Класс исключение, который отвечает за обработку событий,
    когда в Категорию или в Заказ добавляется товар с нулевым количеством.
    """
    def __init__(self, *args):
        self.message = args[0] if args else 'Товар с нулевым количеством не может быть добавлен'

    def __str__(self):
        return self.message
