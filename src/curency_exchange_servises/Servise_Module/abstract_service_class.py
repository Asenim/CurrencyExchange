class AbstractServicesClass:
    def __init__(self, path_data_base=None):
        """
        Абстрактный класс для создания классов сервисов.
        :param path_data_base: Можете передать
        параметром путь к базе данных
        """

        # Создаём путь по умолчанию если пользователем
        # не указан другой путь
        if path_data_base is not None:
            self._path_db = path_data_base
        else:
            self._path_db = "C:\ArhitectFiles\PythonProjects\CurrencyExchange\data_base_directory\currency_db.db"
