import sqlite3
from src.abstract_requests_classes.Abstract_Get_Requests import AbstractGetRequests
import logging


class GetOutputExchangeRates(AbstractGetRequests):

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
                   '%(funcName)s; %(message)s',
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

        try:
            logging.info("Подключение к базе данных прошло успешно")

            # Создается запрос
            __all_data = __cursor.execute(f"""
                SELECT E.ID, C.Code, C2.Code, Rate 
                FROM ExchangeRates E
                JOIN Currencies C on E.BaseCurrencyID = C.ID
                JOIN Currencies C2 on E.TargetCurrencyID = C2.ID;
            """)

            convert_json = self._converter_json_string(__all_data)
            return convert_json

        except sqlite3.Error as error_connected:
            logging.info("Ошибка при работе с SQLite", error_connected)

        finally:
            # Закрываем базу данных
            __cursor.close()
            __data_base.close()

            logging.error("Соединение с базой данных закрыто")

    def get_specific(self, code_currency):
        """
        Метод принимает на вход один аргумент
        строку длиной в 6 символов, первые 3
        символа - это код базовой валюты,
        вторые 3 символа - это код выбранной
        валюты, все символы при этом должны
        быть в верхнем регистре.
        Возвращает json объект в виде строки.
        """

        __data_base = sqlite3.connect(self._path_db)
        __cursor = __data_base.cursor()

        try:
            logging.info("Подключение к базе данных прошло успешно")

            __specific_currency = __cursor.execute(f"""
                SELECT E.ID, C.Code, C2.Code, Rate 
                FROM ExchangeRates E
                JOIN Currencies C on E.BaseCurrencyID = C.ID
                JOIN Currencies C2 on E.TargetCurrencyID = C2.ID
                WHERE C.Code = ? and C2.Code = ?
            """, (code_currency[0:3], code_currency[3:]))

            convert_json = self._converter_json_string(__specific_currency, code_currency=code_currency)
            return convert_json

        except sqlite3.Error as error_connected:
            logging.error("Ошибка при работе с SQLite", error_connected)

        finally:
            __cursor.close()
            __data_base.close()

            logging.info("Соединение с базой данных закрыто")


def test_class():
    db_admin = GetOutputExchangeRates()
    db_admin.get_all()
    db_admin.get_specific('USDEUR')


if __name__ == "__main__":
    test_class()
