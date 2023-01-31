import sqlite3
from src.abstract_requests_classes.abstract_changing_requests_directory.Abstract_Delete_Requests \
    import AbstractDeleteRequests
from src.exchange_rates_request_package.Get_Package.Get_Output_Consolas_Exchange_Rates \
    import GetOutputExchangeRates
import logging


class DeleteConsolasExchangeRates(AbstractDeleteRequests):
    def __init__(self, path_data_base=None):
        """
        Задача класса состоит в том, что бы
        обратиться к таблице с одноименным названием,
        сформировать запрос нужного формата, затем удалить
        информацию, переданную клиентом из базы данных
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

    def delete_information(self, code_currency):
        """
        Метод служит для удаления информации
        в нашей базе данных по переданным параметрам.
        Метод принимает 1 аргумент.
        :param code_currency: Имя принимаемой валюты
            из 6 символов в верхнем регистре.
        :return convert_json: Json объект, который будет
            печатать информацию в консоль и возвращать ее.
        """

        __data_base = sqlite3.connect(self._path_db)
        __cursor = __data_base.cursor()

        try:
            logging.info("Подключение к базе данных прошло успешно")

            # Удаляем информацию из базы данных
            __add_exchange_rates = __cursor.execute(f"""
                DELETE FROM ExchangeRates 
                WHERE (SELECT ID FROM Currencies WHERE Code = ?) = BaseCurrencyID AND
                      (SELECT ID FROM Currencies WHERE Code = ?) = TargetCurrencyID;
                    """, (code_currency[0:3], code_currency[3:]))
            # Коммитим изменения
            __data_base.commit()
            print(f'Данные {code_currency} успешно удалены!')

            # Получаем информацию из базы данных в консоль
            return self._sends_information_to_client(GetOutputExchangeRates(), code_currency)

        except sqlite3.Error as error_connected:
            logging.error("Ошибка при работе с SQLite", error_connected)

        finally:
            __cursor.close()
            __data_base.close()

            logging.info("Соединение с базой данных закрыто")


def test_class():
    delete_object = DeleteConsolasExchangeRates()
    delete_object.delete_information("JPYRUB")


if __name__ == '__main__':
    test_class()
