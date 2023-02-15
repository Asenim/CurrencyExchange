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
