import sqlite3
import logging
import json


class CurrencyExchangeRates:
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

        # Создаём путь по умолчанию если пользователем
        # не указан другой путь
        if path_data_base is not None:
            self._path_db = path_data_base
        else:
            self._path_db = "C:\ArhitectFiles\PythonProjects\CurrencyExchange\data_base_directory\currency_db.db"

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

            if len(__exchange_decode) > 0:
                __result = __exchange_decode[0][0] * amount
                __dict_result = self.__dict_result(base, target, __exchange_decode[0][0], amount, __result)

                __code_currency = base + target
                return self.__converter_json_string(__dict_result, __code_currency)

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
                __dict_result = self.__dict_result(target, base, __reverse_course, amount, __result)

                __code_currency = base + target
                return self.__converter_json_string(__dict_result, __code_currency)

        except IndexError:
            print('Такой валюты в базе данных нет')
            return logging.info('There is no such currency in the database')

        finally:
            # Закрываем базу данных
            __cursor.close()
            __data_base.close()

            logging.error("Соединение с базой данных закрыто")

    def __base_select(self, base_currency):
        """
        Достает информацию о базовой валюте
        из базы данных, нужен для корректного
        вывода в методе exchange_currency
        :param base_currency: Строка длиной
            в 3 символа в верхнем регистре
        :return dict_result: Словарь с нужными
            данными который в дальнейшем конвертируется
            в json строку.
        """
        __data_base = sqlite3.connect(self._path_db)
        __cursor = __data_base.cursor()
        __cursor.execute("""PRAGMA FOREIGN_KEYS = ON;""")

        try:
            logging.info("Подключение к базе данных прошло успешно")

            # Создается запрос
            __base_currency = __cursor.execute("""
                   SELECT * FROM Currencies
                   WHERE Code = ?
                   """, (base_currency,))

            __base_currency_decode = __base_currency.fetchall()
            __dict_result = {
                'id': __base_currency_decode[0][0],
                'name': __base_currency_decode[0][1],
                'code': __base_currency_decode[0][2],
                'sign': __base_currency_decode[0][3]
            }

            return __dict_result

        except sqlite3.Error as err:
            return logging.info(err)

        finally:
            # Закрываем базу данных
            __cursor.close()
            __data_base.close()

            logging.error("Соединение с базой данных закрыто")

    def __target_select(self, target_currency):
        """
        Достает информацию о базовой валюте
        из базы данных, нужен для корректного
        вывода в методе exchange_currency
        :param target_currency: Строка длиной
            в 3 символа в верхнем регистре
        :return dict_result: Словарь с нужными
            данными который в дальнейшем конвертируется
            в json строку.
        """

        __data_base = sqlite3.connect(self._path_db)
        __cursor = __data_base.cursor()
        __cursor.execute("""PRAGMA FOREIGN_KEYS = ON;""")

        try:
            logging.info("Подключение к базе данных прошло успешно")

            # Создается запрос
            __target_currency = __cursor.execute("""
                               SELECT * FROM Currencies
                               WHERE Code = ?
                               """, (target_currency,))

            __target_currency_decode = __target_currency.fetchall()
            __dict_result = {
                'id': __target_currency_decode[0][0],
                'name': __target_currency_decode[0][1],
                'code': __target_currency_decode[0][2],
                'sign': __target_currency_decode[0][3]
            }

            return __dict_result

        except sqlite3.Error as err:
            return logging.info(err)

        finally:
            # Закрываем базу данных
            __cursor.close()
            __data_base.close()

    def __dict_result(self, base_curr, target_curr, rate, amount, result):
        """

        :param base_curr: Базовая валюта
        :param target_curr: Избранная валюта
        :param rate: Текущий курс
        :param amount: Сколько меняем
        :param result: Готовый результат обмена
        :return __dicts_result: Готовый словарь с данными
        """
        __base_currency = self.__base_select(base_curr)
        __target_currency = self.__target_select(target_curr)
        __dicts_result = {
            'BaseCurrency': __base_currency,
            'TargetCurrency': __target_currency,
            'Rate': rate,
            'Amount': amount,
            'ConvertedAmount': result
        }

        return __dicts_result

    @staticmethod
    def __converter_json_string(object_db, code_currency=None):
        """
        Метод конвертирует информацию из запросов
        в json строку и возвращает эту самую строку
        для отображения.
        :param object_db: Принимает на вход объект базы данных.
        :param code_currency: Принимает на вход код валюты
        :return: json строка/объект
        """
        __decode_data = object_db
        __data_json = json.dumps(__decode_data, sort_keys=False, indent=4, ensure_ascii=False)

        if len(__data_json) <= 2:
            print(f'Информации о валюте {code_currency} в базе данных нет')
            return f'There is no information about the currency {code_currency} in the database'
        else:
            print(__data_json)
            return __data_json


def test_class():
    db_admin = CurrencyExchangeRates()
    db_admin.exchange_currency('RUB', 'TRY', 10)
    db_admin.exchange_currency('TRY', 'RUB', 10)
    db_admin.exchange_currency('KZH', 'SGP', 12)


if __name__ == "__main__":
    test_class()
