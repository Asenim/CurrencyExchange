import json


class AbstractRequests:
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

    @staticmethod
    def _converter_json_string(object_db):
        """
        Метод конвертирует информацию из запросов
        в json строку и возвращает эту самую строку
        для отображения.
        :param object_db: Принимает на вход объект базы данных
        :return: json строка/объект
        """
        __decode_data = object_db.fetchall()
        __data_json = json.dumps(__decode_data, indent=6, ensure_ascii=False)

        if len(__data_json) <= 2:
            print('Такой информации в базе данных нет')
            return 'Такой информации в базе данных нет'
        else:
            print(__data_json)
            return __data_json
