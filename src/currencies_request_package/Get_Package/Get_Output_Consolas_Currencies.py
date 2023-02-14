import sqlite3
from src.abstract_requests_classes.Abstract_Get_Requests import AbstractGetRequests
import logging


class GetOutputCurrencies(AbstractGetRequests):

    def __init__(self, path_data_base=None):
        """
        Задача класса состоит в том, что бы
        обратиться к таблице с одноименным названием,
        сформировать запрос нужного формата и
        отправить этот запрос клиенту.
        :param path_data_base: Можете передать
        параметром путь к базе данных
        """
        super().__init__(path_data_base)

        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s; %(levelname)s; '
                   '%(module)s; %(lineno)s; '
                   '%(funcName)s; %(message)s'
        )
        logging.getLogger(__name__)

    def get_all(self):
        """
        Метод обращается к базе данных
        достает от туда всю необходимую
        информацию из таблицы, после чего
        отправляет ее в консоль клиенту и
        возвращает json объект в виде строки.
        """
        # Происходит подключение к базе данных
        __data_base = sqlite3.connect(self._path_db)
        __cursor = __data_base.cursor()
        __cursor.execute("""PRAGMA FOREIGN_KEYS = ON;""")

        try:
            logging.info("Подключение к базе данных прошло успешно")

            # Создается запрос
            __all_data = __cursor.execute(f"""
                SELECT * FROM Currencies;
            """)
            __all_data_decode = __all_data.fetchall()
            __dict_all = self.dict_result_all(__all_data_decode)

            convert_json = self._converter_json_string(__dict_all)
            return convert_json

        except sqlite3.Error as error_connected:
            logging.error("Ошибка при работе с SQLite", error_connected)

        finally:
            __cursor.close()
            __data_base.close()

            logging.info("Соединение с базой данных закрыто")

    def get_specific(self, code_currency):
        """
        Метод принимает на вход один аргумент
        строку длиной в 3 символа, которые
        являются кодом валюты, все символы при
        этом должны быть в верхнем регистре.
        Возвращает json объект в виде строки.
        """
        __data_base = sqlite3.connect(self._path_db)
        __cursor = __data_base.cursor()
        __cursor.execute("""PRAGMA FOREIGN_KEYS = ON;""")

        try:
            logging.info("Подключение к базе данных прошло успешно")

            __specific_currency = __cursor.execute(f"""
                SELECT * FROM Currencies
                WHERE Code = ?;
            """, (code_currency,))

            __specific_decode = __specific_currency.fetchall()
            __dict_result = self.dict_result_specific(__specific_decode)

            convert_json = self._converter_json_string(__dict_result, code_currency=code_currency)
            return convert_json

        except sqlite3.Error as error_connected:
            logging.error("Ошибка при работе с SQLite", error_connected)

        finally:
            __cursor.close()
            __data_base.close()

            logging.info("Соединение с базой данных закрыто")

    @staticmethod
    def dict_result_all(list_object):
        __list_result = []
        __list_data = list_object

        for element in __list_data:
            __list_result.append({
                'id': element[0],
                'name': element[1],
                'code': element[2],
                'sign': element[3]
                                         })

        return __list_result

    @staticmethod
    def dict_result_specific(list_object):
        __dict_result = {}
        __list_data = list_object

        __dict_result['id'] = __list_data[0][0]
        __dict_result['name'] = __list_data[0][1]
        __dict_result['code'] = __list_data[0][2]
        __dict_result['sign'] = __list_data[0][3]

        return __dict_result


def test_class():

    db_admin = GetOutputCurrencies()
    db_admin.get_all()
    db_admin.get_specific('USD')


if __name__ == "__main__":
    test_class()
