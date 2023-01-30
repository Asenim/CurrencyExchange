from abc import *
from scr.abstract_requests_classes.abstract_changing_requests_directory.Abstract_Changing_Requests\
    import AbstractChangingRequests


class AbstractDeleteRequests(AbstractChangingRequests, ABC):

    @abstractmethod
    def __init__(self, path_data_base=None):
        """
        Абстрактный класс который позволяет работать
        с классами delete запросов.
        Данные классы отправляют запрос в базу данных и
        удаляют из базы переданную запросом информацию,
        после чего отравляют ответ пользователю об успехе или
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
    def delete_information(self, arg1):
        """
        Данный метод удаляет из базы данных информацию
        по заданным аргументам, в зависимости от таблицы
        содержание и тип аргументов может сильно различаться
        Поэтому в данном классе не будет описания аргументов
        P.S. ID в таблице назначается - автоматически.
        """
        pass
