from abc import *


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
            self._path_db = 'C:/ArhitectFiles/PythonProjects/CurrencyExchange/scr/data_base_directory/admin_db.db'
