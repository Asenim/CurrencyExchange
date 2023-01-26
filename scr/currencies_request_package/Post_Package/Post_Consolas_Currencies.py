import sqlite3
from scr.abstract_requests_classes.Abstract_Post_Requests import AbstractPostRequests
from scr.currencies_request_package.Get_Package.Get_Output_Consolas_Currencies import GetOutputCurrencies


class PostConsolasCurrencies(AbstractPostRequests):

    def __init__(self, path_data_base=None):

        super().__init__(path_data_base)

    def post_information(self, code_arg, fullname_arg, sign_arg):

        # Подключаемся к базе данных
        __data_base = sqlite3.connect(self._path_db)
        __cursor = __data_base.cursor()

        try:

            print("Подключение к базе данных прошло успешно")

            # Добавляем информацию в базу данных
            __add_currency = __cursor.execute("""
                INSERT INTO Currencies(Code, FullName, Sign)
                VALUES(?, ?, ?)
            """, (code_arg, fullname_arg, sign_arg))

            # Коммитим изменения
            __data_base.commit()

            # Получаем информацию из базы данных в консоль
            get_information = GetOutputCurrencies()
            get_information.get_specific(code_arg)

        except sqlite3.Error as error_connected:

            print("Ошибка при работе с SQLite", error_connected)

        finally:
            __cursor.close()
            __data_base.close()

            print("Соединение закрыто")


def test_class():
    post_consolas_currencies = PostConsolasCurrencies()
    post_consolas_currencies.post_information('JPY', 'Yen', 'Y')


if __name__ == "__main__":
    test_class()
