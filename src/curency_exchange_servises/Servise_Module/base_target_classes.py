import sqlite3
import logging
from src.curency_exchange_servises.Servise_Module.abstract_service_class \
    import AbstractServicesClass


class BaseTargetClasses(AbstractServicesClass):
    def __init__(self, path_data_base=None):
        """
        Данный класс является модулем и не
        используется вне класса Сервисов.
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

    def base_select(self, base_currency):
        """
        Достает информацию о базовой валюте
        из базы данных, нужен для корректного
        вывода в методе exchange_currency
        :param base_currency: Строка длиной
            в 3 символа в верхнем регистре.
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

    def target_select(self, target_currency):
        """
        Достает информацию о базовой валюте
        из базы данных, нужен для корректного
        вывода в методе exchange_currency
        :param target_currency: Строка длиной
            в 3 символа в верхнем регистре.
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
