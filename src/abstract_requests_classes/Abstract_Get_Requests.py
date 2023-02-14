from abc import *
import json
from src.abstract_requests_classes.Abstract_Requests import AbstractRequests


class AbstractGetRequests(AbstractRequests, ABC):

    @abstractmethod
    def __init__(self, path_data_base=None):
        """
        Абстрактный класс который позволяет работать
        с классами get запросов.
        Данные классы обращаются к базе данных
        вытаскивают от туда информацию, после
        чего отравляют пользователю и возвращают
        в формате json.
            P.S. В зависимости от реализации отправка осуществляется
            в консоль или же в браузер.

        """
        super().__init__(path_data_base)

    @abstractmethod
    def get_all(self):
        """
        Метод обращается к базе данных и
        вытаскивает от туда всю
        информацию, после чего
        выводит ее в консоль и возвращает.
        :return data_json: Json Объект.
        """
        pass

    @abstractmethod
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
        __data_json = json.dumps(__data_object, sort_keys=True, indent=4, ensure_ascii=False)

        if len(__data_json) <= 2:
            print(f'Информации о валюте {code_currency} в базе данных нет')
            return f'There is no information about the currency {code_currency} in the database'
        else:
            print(__data_json)
            return __data_json
