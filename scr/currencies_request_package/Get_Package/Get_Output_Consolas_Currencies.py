import sqlite3
from scr.abstract_requests_classes.Abstract_Get_Requests import AbstractGetRequests


class GetOutputCurrencies(AbstractGetRequests):

    def __init__(self, path_data_base=None):

        super().__init__(path_data_base)

    def get_all(self):

        try:

            # Происходит подключение к базе данных
            __data_base = sqlite3.connect(self._path_db)
            __cursor = __data_base.cursor()

            print("Подключение к базе данных прошло успешно")

            # Создается запрос
            __all_data = __cursor.execute(f"""
                SELECT * FROM Currencies;
            """)
            self._converter_json_string(__all_data)

            # Закрываем базу данных
            if __data_base:
                __cursor.close()
                __data_base.close()

                print("Соединение с базой данных закрыто")

        except sqlite3.Error as error_connected:

            print("Ошибка при работе с SQLite", error_connected)

    def get_specific(self, code_currency):

        try:

            __data_base = sqlite3.connect(self._path_db)
            __cursor = __data_base.cursor()

            print("Подключение к базе данных прошло успешно")

            specific_currency = __cursor.execute(f"""
                SELECT * FROM Currencies
                WHERE Code = ?;
            """, (code_currency,))
            self._converter_json_string(specific_currency)

            if __data_base:
                __cursor.close()
                __data_base.close()

                print("Соединение с базой данных закрыто")

        except sqlite3.Error as error_connected:

            print("Ошибка при работе с SQLite", error_connected)


def test_class():

    path = 'C:/ArhitectFiles/PythonProjects/CurrencyExchange/scr/data_base_directory/admin_db.db'
    db_admin = GetOutputCurrencies(path)
    db_admin.get_all()
    db_admin.get_specific('RUB')


if __name__ == "__main__":
    test_class()
