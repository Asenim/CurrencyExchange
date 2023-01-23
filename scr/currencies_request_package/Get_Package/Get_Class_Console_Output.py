import sqlite3
import json


class GetOutputCurrencies:
    def __init__(self, path_data_base=None):
        """
        Класс работает с базой данных
        вытаскивает из него информацию
        и показывает пользователю.
        :param path_data_base: Принимает полный путь до
            базы данных. P.S. Класс принимает путь по умолчанию
            для работы с базой данных, если в аргумент не передан
            путь.
        """
        if path_data_base is not None:
            self.__path_db = path_data_base
        else:
            self.__path_db = 'C:/ArhitectFiles/PythonProjects/CurrencyExchange/scr/data_base_directory/admin_db.db'

    def get_all_currency(self):
        """
        Метод обращается к базе данных и
        вытаскивает от туда всю
        информацию, после чего
        выводит ее в консоль и возвращает.
        :return data_json: Json Объект.
        """
        # Происходит подключение к базе данных
        __data_base = sqlite3.connect(self.__path_db)
        __cursor = __data_base.cursor()

        # Создается запрос
        __all_data = __cursor.execute(f"""
        SELECT * FROM Currencies;
        """)
        self.__converter_json_string(__all_data)

        # Закрываем базу данных
        __cursor.close()
        __data_base.close()

    def get_specific_currency(self, id_currency):
        """
        Метод по выбранным параметрам обращается к
        базе данных и выдает в консоль
        информацию по конкретной валюте.
        :param id_currency: Параметр принимает id
            запрашиваемой валюты
        """
        __data_base = sqlite3.connect(self.__path_db)
        __cursor = __data_base.cursor()

        specific_currency = __cursor.execute(f"""
        SELECT * FROM Currencies
        WHERE ID = {id_currency};
        """)
        self.__converter_json_string(specific_currency)

        __cursor.close()
        __data_base.close()

    @staticmethod
    def __converter_json_string(object_db):
        """
        Внутренний метод класса который позволяет конвертировать
        объекты из базы данных в json объекты и выводить их на экран
        консоли.
        :param object_db:
        :return:
        """
        decode_data = object_db.fetchall()
        data_json = json.dumps(decode_data, indent=6, ensure_ascii=False)
        print(data_json)
        return data_json


def test_class():
    path = 'C:/ArhitectFiles/PythonProjects/CurrencyExchange/scr/data_base_directory/admin_db.db'
    db_admin = GetOutputCurrencies(path)
    db_admin.get_all_currency()
    db_admin.get_specific_currency("2")


if __name__ == "__main__":
    test_class()
