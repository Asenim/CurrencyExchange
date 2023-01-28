import sqlite3
from scr.abstract_requests_classes.abstract_changing_requests_directory.Abstract_Patch_Requests\
    import AbstractPatchRequest
from scr.exchange_rates_request_package.Get_Package.Get_Output_Consolas_Exchange_Rates \
    import GetOutputExchangeRates


class PatchConsolasExchangeRates(AbstractPatchRequest):
    def __init__(self, path_data_base=None):
        """
        Задача класса состоит в том, что бы
        обратиться к таблице с одноименным названием,
        сформировать запрос нужного формата, затем изменить
        информацию в базе данных по переданным клиентом аргументам
        и отправить результат изменения данных в базе - клиенту.
        :param path_data_base: Можете передать
            параметром путь к базе данных
        """
        super().__init__(path_data_base)

    def change_column(self, code_arg, meaning, change_column='Rate'):
        """
        Метод служит для изменения информации
        в нашей базе данных по переданным параметрам.
        Метод принимает 2 аргумента.
        :param change_column: Дополнительный параметр для
            изменения конкретного столбца, по умолчанию стоит
            необходимый параметр для изменения конкретного столбца
            без острой необходимости - не изменять.
        :param code_arg: Имя принимаемой валюты
            из 6 символов в верхнем регистре.
        :param meaning: Значение на которое будем изменять.
        :return convert_json: Json объект, который будет
            печатать информацию в консоль и возвращать ее.
        """
        __data_base = sqlite3.connect(self._path_db)
        __cursor = __data_base.cursor()

        try:
            print("Подключение к базе данных прошло успешно")

            # Изменяем информацию в базе данных
            __add_exchange_rates = __cursor.execute(f"""
                UPDATE ExchangeRates SET {change_column} = ?
                WHERE (SELECT ID FROM Currencies WHERE Code = ?) = BaseCurrencyID AND
                      (SELECT ID FROM Currencies WHERE Code = ?) = TargetCurrencyID;
            """, (meaning, code_arg[0:3], code_arg[3:]))
            # Коммитим изменения
            __data_base.commit()
            print(f'Данные {code_arg} в столбце {change_column}'
                  f'успешно изменены!')

            # Получаем информацию из базы данных в консоль
            return self._sends_information_to_client(GetOutputExchangeRates(), code_arg)

        except sqlite3.Error as error_connected:
            print("Ошибка при работе с SQLite", error_connected)

        finally:
            __cursor.close()
            __data_base.close()

            print("Соединение закрыто")


def test_class():
    change_object = PatchConsolasExchangeRates()
    change_object.change_column("RUBJPY", 1.85)


if __name__ == '__main__':
    test_class()
