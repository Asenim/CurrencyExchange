class AbstractGetRequests:
    def __init__(self, path_data_base=None):
        """
        Класс работает с базой данных
        вытаскивает из него информацию
        и показывает пользователю.
        :param path_data_base: Принимает полный путь до
            базы данных. P.S. Класс принимает путь по умолчанию
            для работы с базой данных, если в аргумент не передан
            путь.
        """
        if path_data_base is not None:
            self._path_db = path_data_base
        else:
            self._path_db = 'C:/ArhitectFiles/PythonProjects/CurrencyExchange/scr/data_base_directory/admin_db.db'

    def get_all(self):
        """
        Метод обращается к базе данных и
        вытаскивает от туда всю
        информацию, после чего
        выводит ее в консоль и возвращает.
        :return data_json: Json Объект.
        """
        pass

    def get_specific(self, code_currency):
        """
        Метод по выбранным параметрам обращается к
        базе данных и выдает в консоль
        информацию по конкретной валюте.
        :param code_currency: Параметр принимает код
            запрашиваемой валюты
        """
        pass

    @staticmethod
    def _converter_json_string(object_db):
        """
        Метод конвертирует информацию из запросов
        в json строку и возвращает эту самую строку
        для отображения.
        :param object_db: Принимает на вход объект базы данных
        :return: json строка/объект
        """
        pass
