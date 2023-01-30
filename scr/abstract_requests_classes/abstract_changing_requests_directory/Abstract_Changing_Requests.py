from scr.abstract_requests_classes.Abstract_Requests import AbstractRequests
from abc import *


class AbstractChangingRequests(AbstractRequests, ABC):

    @abstractmethod
    def __init__(self, path_data_base=None):
        super().__init__(path_data_base)

    @staticmethod
    def _sends_information_to_client(get_class, return_result):
        """
        Задача метода состоит в том
        что бы вернуть клиенту результат
        выполнения запросов которые изменяют
        данные в таблице.
        :param get_class: Передается объект класса.
        :param return_result: Передаётся конвертируемый объект.
            Чаще всего это распарсенный код валюты.
        :return convert_json: Возвращается сконвертированный объект.
        """
        get_information = get_class
        convert_json = get_information.get_specific(return_result)
        return convert_json
