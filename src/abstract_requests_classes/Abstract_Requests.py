from abc import *
import json


class AbstractRequests(ABC):

    @abstractmethod
    def __init__(self, path_data_base=None):
        """
        Абстрактный класс для создания классов запросов.
        :param path_data_base: Принимает полный путь до
            базы данных. P.S. Класс принимает путь по умолчанию
            для работы с базой данных, если в аргумент не передан
            путь.
        """
        if path_data_base is not None:
            self._path_db = path_data_base
        else:
            self._path_db = "C:\ArhitectFiles\PythonProjects\CurrencyExchange\data_base_directory\currency_db.db"

    @staticmethod
    def _converter_json_string(data_object, code_currency=None):
        """
        Метод конвертирует информацию из запросов
        в json строку и возвращает эту самую строку
        для отображения.
        :param data_object: Принимает на вход объект данных
            в формате dict.
        :param code_currency: Принимает на вход код валюты.
        :return: json строка/объект.
        """
        __data_object = data_object
        __data_json = json.dumps(__data_object, indent=4, ensure_ascii=False)

        if len(__data_json) <= 2:
            print(f'Информации о валюте {code_currency} в базе данных нет')
            return f'There is no information about the currency {code_currency} in the database'
        else:
            print(__data_json)
            return __data_json
