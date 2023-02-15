import sqlite3
import logging
from src.abstract_requests_classes.Abstract_Get_Requests import AbstractGetRequests
from src.curency_exchange_servises.Servise_Module.base_target_classes import BaseTargetClasses


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
                SELECT E.ID, C.Code, C2.Code, Rate 
                FROM ExchangeRates E
                JOIN Currencies C on E.BaseCurrencyID = C.ID
                JOIN Currencies C2 on E.TargetCurrencyID = C2.ID;
            """)

            __all_data_decode = __all_data.fetchall()
            __dict_result = self.dict_all_result(__all_data_decode)

            __convert_json = self._converter_json_string(__dict_result)
            return __convert_json

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
        __cursor.execute("""PRAGMA FOREIGN_KEYS = ON;""")

        try:
            logging.info("Подключение к базе данных прошло успешно")

            try:
                __specific_currency = __cursor.execute(f"""
                    SELECT E.ID, C.Code, C2.Code, Rate 
                    FROM ExchangeRates E
                    JOIN Currencies C on E.BaseCurrencyID = C.ID
                    JOIN Currencies C2 on E.TargetCurrencyID = C2.ID
                    WHERE C.Code = ? and C2.Code = ?
                """, (code_currency[0:3], code_currency[3:]))

                __specific_currency_decode = __specific_currency.fetchall()
                __dict_result = self.dict_specific_result(__specific_currency_decode)

                __convert_json = self._converter_json_string(__dict_result, code_currency=code_currency)
                return __convert_json

            except IndexError as err:
                error_message = {
                    code_currency: '!!!Course not found!!!'
                }
                logging.info(f'Курс не найден, {err}')

                return self._converter_json_string(error_message)


        except sqlite3.Error as error_connected:
            logging.error("Ошибка при работе с SQLite", error_connected)

        finally:
            __cursor.close()
            __data_base.close()

            logging.info("Соединение с базой данных закрыто")

    @staticmethod
    def dict_all_result(object_db):
        __list_result = []
        __data_list = object_db

        for element in __data_list:
            bt_object = BaseTargetClasses()
            __base_currency = bt_object.base_select(element[1])
            __target_currency = bt_object.target_select(element[2])
            __list_result.append({
                'Id': element[0],
                'BaseCurrency': __base_currency,
                'TargetCurrency': __target_currency,
                'Rate': element[3]
            })

        return __list_result

    @staticmethod
    def dict_specific_result(object_db):
        """
        Формирует словарь который в следствии будет конвертирован
        в json объект/файл.
        Конвертация происходит не в этом методе.
        :param object_db: объект базы данных.
        :return __dicts_result: Готовый словарь с данными.
        """
        bt_object = BaseTargetClasses()
        __data_list = object_db
        __base_currency = bt_object.base_select(__data_list[0][1])
        __target_currency = bt_object.target_select(__data_list[0][2])
        __dicts_result = {
            'Id': __data_list[0][0],
            'BaseCurrency': __base_currency,
            'TargetCurrency': __target_currency,
            'Rate': __data_list[0][3]
        }

        return __dicts_result


def test_class():
    db_admin = GetOutputExchangeRates()
    db_admin.get_all()
    db_admin.get_specific('USDEUR')
    db_admin.get_specific('USDKUR')


if __name__ == "__main__":
    test_class()
