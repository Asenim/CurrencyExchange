import sqlite3
from src.abstract_requests_classes.abstract_changing_requests_directory.Abstract_Post_Requests \
    import AbstractPostRequests
from src.exchange_rates_request_package.Get_Package.Get_Output_Consolas_Exchange_Rates \
    import GetOutputExchangeRates
import logging


class PostConsolasExchangeRates(AbstractPostRequests):
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

        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s; %(levelname)s; '
                   '%(module)s; %(lineno)s; '
                   '%(funcName)s; %(message)s'
        )
        logging.getLogger(__name__)

    def post_information(self, base_name, target_name, rate):
        """
        Метод служит для отправки информации
        которую передал клиент для отправки
        в нашу удаленную базу данных.
        Метод принимает 3 аргумента.
        :param base_name: Имя базовой валюты
        :param target_name: Имя Выбранной валюты
        :param rate: Курс который мы хотим добавить в БД.
        :return convert_json: Json объект, который был
        сформирован в методе.
        """
        # Подключаемся к базе данных
        __data_base = sqlite3.connect(self._path_db)
        __cursor = __data_base.cursor()
        __cursor.execute("""PRAGMA FOREIGN_KEYS = ON;""")

        try:
            logging.info("Подключение к базе данных прошло успешно")

            # Добавляем информацию в базу данных
            __add_exchange_rates = __cursor.execute("""
                INSERT INTO ExchangeRates(BaseCurrencyID, TargetCurrencyID, Rate)
                VALUES((SELECT ID FROM Currencies WHERE Code = ?),
                        (SELECT ID FROM Currencies WHERE Code = ?), ?)
            """, (base_name, target_name, rate))
            # Коммитим изменения
            __data_base.commit()
            print(f'В базу данных добавлен новый курс {base_name}/{target_name}')

            # Получаем информацию из базы данных в консоль
            get_request = base_name + target_name
            return self._sends_information_to_client(GetOutputExchangeRates(), get_request)

        except sqlite3.Error as error_connected:
            logging.error("Ошибка при работе с SQLite", error_connected)

        finally:
            __cursor.close()
            __data_base.close()

            logging.info("Соединение с базой данных закрыто")


def test_class():
    post_request = PostConsolasExchangeRates()
    post_request.post_information('JPY', 'RUB', 0.53)


if __name__ == '__main__':
    test_class()
