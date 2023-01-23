from scr.abstract_requests_classes.Abstract_Requests import AbstractRequests


class AbstractGetRequests(AbstractRequests):

    def __init__(self, path_data_base=None):

        super().__init__(path_data_base)

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
