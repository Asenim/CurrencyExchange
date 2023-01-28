import sqlite3
from scr.abstract_requests_classes.abstract_changing_requests_directory.Abstract_Post_Requests \
    import AbstractPostRequests
from scr.currencies_request_package.Get_Package.Get_Output_Consolas_Currencies import GetOutputCurrencies


class PostConsolasCurrencies(AbstractPostRequests):

    def __init__(self, path_data_base=None):
        """
        Задача класса состоит в том, что бы
        обратиться к таблице с одноименным названием,
        сформировать запрос нужного формата, затем добавить
        информацию, переданную клиентом в базу данных
        и отправить результат этого запроса - клиенту.
        :param path_data_base: Можете передать
        параметром путь к базе данных
        """
        super().__init__(path_data_base)

    def post_information(self, code_arg, fullname_arg, sign_arg):
        """
        Метод служит для отправки информации
        которую передал клиент для отправки
        в нашу удаленную базу данных.
        Метод принимает 3 аргумента.
        :param code_arg: Код валюты
        :param fullname_arg: Полное имя валюты
        :param sign_arg: Знак\Сигнатура валюты
        :return convert_json: json объект который был
        сформирован в методе.
        """
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
            return self._sends_information_to_client(GetOutputCurrencies(), code_arg)

        except sqlite3.Error as error_connected:
            print("Ошибка при работе с SQLite", error_connected)

        finally:
            __cursor.close()
            __data_base.close()

            print("Соединение закрыто")


def test_class():
    post_consolas_currencies = PostConsolasCurrencies()
    post_consolas_currencies.post_information('KZH', 'Tenge', 'T')


if __name__ == "__main__":
    test_class()
