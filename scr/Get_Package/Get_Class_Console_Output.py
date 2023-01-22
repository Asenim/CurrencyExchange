import json


class GetOutput:
    def __init__(self, data_base):
        """
        Класс работает с базой данных
        вытаскивает из него информацию
        и показывает пользователю.
        :param data_base:
        """
        self.__data_base = data_base
        self.__cursor = self.__data_base.cursor()

    def get_all_currency(self, table_name):
        """
        Метод обращается к базе данных и
        вытаскивает от туда всю
        информацию, после чего
        выводит ее в консоль и возвращает.
        :param table_name: Имя таблицы с которой мы работаем
        :return data_json: json Объект
        """

        all_data = self.__cursor.execute(f"""
        SELECT * FROM {table_name};
        """)
        python_data = all_data.fetchall()
        data_json = json.dumps(python_data, indent=6, ensure_ascii=False)
        print(data_json)
        return data_json

    def get_specific_currency(self, table_name, code_currency):
        """
        Метод по выбранным параметрам обращается к
        базе данных и выдает в консоль
        информацию по конкретной валюте.
        :param table_name: Имя таблицы с которой мы работаем.
        :param code_currency: Код валюты которую мы хотим получить.
        :return:
        """
        pass
