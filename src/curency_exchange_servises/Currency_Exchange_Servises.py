import sqlite3
import logging
from src.curency_exchange_servises.Servise_Module import *


class CurrencyExchangeRates(AbstractServicesClass):
    def __init__(self, path_data_base=None):
        """
        Задача класса состоит в том, что бы
        обратиться к базе данных, затем перевести
        определенное количество одной валюты
        в другую и отправить клиенту результат
        работы этого метода в формате json.
        :param path_data_base: Можете передать
        параметром путь к базе данных
        """
        super().__init__(path_data_base)

        # Конфигурация логов
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s; %(levelname)s; '
                   '%(module)s; %(lineno)s; '
                   '%(funcName)s; %(message)s'
        )
        logging.getLogger(__name__)

    def exchange_currency(self, base, target, amount):
        """
        Метод для расчета перевода одной валюты
        в другую.
        :param base: "BaseCurrency" аргумент
            для обращения в БД для того что бы
            вытащить значение "Rate"
            (текущего курса) принимает на вход
            строку длиною в 3 символа в верхнем
            регистре.
        :param target: "TargetCurrency" аргумент
            аналогичен base.
        :param amount: Принимает на вход число
            которое будет умножаться на курс валют
            (Rate)
        :return:
        """

        __data_base = sqlite3.connect(self._path_db)
        __cursor = __data_base.cursor()
        __cursor.execute("""PRAGMA FOREIGN_KEYS = ON;""")

        try:
            logging.info("Подключение к базе данных прошло успешно")

            # Создается запрос
            __exchange = __cursor.execute("""
                SELECT Rate FROM ExchangeRates
                WHERE (SELECT ID FROM Currencies WHERE Code = ?) = BaseCurrencyID
                  and (SELECT ID FROM Currencies WHERE Code = ?) = TargetCurrencyID;
            """, (base, target))

            __exchange_decode = __exchange.fetchall()
            # Является импортированным модулем
            __result_data = ResultDataJson()

            if len(__exchange_decode) > 0:
                __result = float(__exchange_decode[0][0]) * float(amount)
                __dict_result = __result_data.dict_convert_result(base, target, __exchange_decode[0][0], amount, __result)

                __code_currency = base + target
                return __result_data.converter_json_string(__dict_result, __code_currency)

            else:
                # Создается запрос
                __exchange = __cursor.execute("""
                     SELECT Rate FROM ExchangeRates
                     WHERE (SELECT ID FROM Currencies WHERE Code = ?) = BaseCurrencyID
                       and (SELECT ID FROM Currencies WHERE Code = ?) = TargetCurrencyID;
                 """, (target, base))

                __exchange_decode = __exchange.fetchall()
                __reverse_course = 1 // __exchange_decode[0][0]
                __result = __reverse_course * amount
                __dict_result = __result_data.dict_convert_result(target, base, __reverse_course, amount, __result)

                __code_currency = base + target
                return __result_data.converter_json_string(__dict_result, __code_currency)

        except IndexError:
            print('Такой валюты в базе данных нет')
            return logging.info('There is no such currency in the database')

        finally:
            # Закрываем базу данных
            __cursor.close()
            __data_base.close()

            logging.error("Соединение с базой данных закрыто")


def test_class():
    db_admin = CurrencyExchangeRates()
    db_admin.exchange_currency('RUB', 'TRY', 10)
    db_admin.exchange_currency('TRY', 'RUB', 10)
    db_admin.exchange_currency('KZH', 'SGP', 12)


if __name__ == "__main__":
    test_class()
