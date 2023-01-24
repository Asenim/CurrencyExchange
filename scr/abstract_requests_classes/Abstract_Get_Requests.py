from abc import *
import json
from scr.abstract_requests_classes.Abstract_Requests import AbstractRequests


class AbstractGetRequests(AbstractRequests, ABC):

    @abstractmethod
    def __init__(self, path_data_base=None):

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
    def _converter_json_string(object_db):
        __decode_data = object_db.fetchall()
        __data_json = json.dumps(__decode_data, indent=6, ensure_ascii=False)

        if len(__data_json) <= 2:
            print('Такой информации в базе данных нет')
            return 'Такой информации в базе данных нет'
        else:
            print(__data_json)
            return __data_json
