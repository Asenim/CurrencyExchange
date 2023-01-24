from abc import *
from scr.abstract_requests_classes.Abstract_Requests import AbstractRequests


class AbstractPostRequests(AbstractRequests, ABC):

    @abstractmethod
    def __init__(self, path_data_base=None):
        """
        Абстрактный класс который позволяет работать
        с классами post запросов.
        Данные классы отправляют запрос в базу данных и
        добавляют в базу переданную информацию, после
        чего отравляют ответ пользователю об успехе или
        ошибке и возвращают его в формате json.
            P.S. В зависимости от реализации отправка осуществляется
            в консоль или же в браузер.
        :param path_data_base: Принимает полный путь до
            базы данных. P.S. Класс принимает путь по умолчанию
            для работы с базой данных, если в аргумент не передан
            путь.
        """

        super().__init__(path_data_base)

    @abstractmethod
    def post_information(self, arg1, arg2, arg3):
        """
        Данный метод добавляет в базу данных информацию
        по заданным аргументам, в зависимости от таблицы
        содержание и тип аргументов может сильно различаться
        Поэтому в данном классе не будет описания аргументов
        P.S. ID в таблице назначается - автоматически.
        """
        pass

    @staticmethod
    def _converter_json_string(object_db):
        pass