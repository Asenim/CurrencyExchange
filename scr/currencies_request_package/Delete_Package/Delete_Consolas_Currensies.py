import sqlite3
from scr.currencies_request_package.Get_Package.Get_Output_Consolas_Currencies import GetOutputCurrencies
from scr.abstract_requests_classes.abstract_changing_requests_directory.Abstract_Delete_Requests \
    import AbstractDeleteRequests


class DeleteConsolasCurrencies(AbstractDeleteRequests):
    def __init__(self, path_data_base=None):
        """
        Задача класса состоит в том, что бы
        обратиться к таблице с одноименным названием,
        сформировать запрос нужного формата, затем
        удалить информацию, из базы данных затем
        отправить результат этого запроса - клиенту.
        :param path_data_base: Можете передать
        параметром путь к базе данных
        """
        super().__init__(path_data_base)

    def delete_information(self, code_currency):
        """
        Метод служит для удаления информации
        в нашей базе данных по переданным параметрам.
        Метод принимает 1 аргумент.
        :param code_currency: Имя принимаемой валюты
            из 3 символов в верхнем регистре.
        :return convert_json: Json объект, который будет
            печатать информацию в консоль и возвращать ее.
        """
        # Подключаемся к базе данных
        __data_base = sqlite3.connect(self._path_db)
        __cursor = __data_base.cursor()

        try:

            print("Подключение к базе данных прошло успешно")

            # Удаляем информацию из базы данных
            __add_currency = __cursor.execute("""
                        DELETE FROM Currencies
                        WHERE Code = ?
                    """, (code_currency,))

            # Коммитим изменения
            print(f'Данные {code_currency} успешно удалены!')
            __data_base.commit()

            # Получаем информацию из базы данных в консоль
            return self._sends_information_to_client(GetOutputCurrencies(), code_currency)

        except sqlite3.Error as error_connected:
            print("Ошибка при работе с SQLite", error_connected)

        finally:
            __cursor.close()
            __data_base.close()

            print("Соединение c базой данных закрыто")


def test_class():
    delete_consolas_currencies = DeleteConsolasCurrencies()
    delete_consolas_currencies.delete_information('KZH')


if __name__ == '__main__':
    test_class()