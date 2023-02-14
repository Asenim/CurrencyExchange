import json
from src.curency_exchange_servises.Servise_Module import *


class ResultDataJson(AbstractServicesClass):
    def __init__(self, path_data_base=None):
        """
        Данный класс является модулем и не
        используется вне класса Сервисов.
        Задача класса состоит в том что бы формировать
        словари, после чего формировать из этих словарей
        json объекты.
        :param path_data_base: Можете передать
        параметром путь к базе данных
        """
        super().__init__(path_data_base)

    @staticmethod
    def dict_convert_result(base_curr, target_curr, rate, amount, result):
        """
        Формирует словарь который в следствии будет конвертирован
        в json объект/файл.
        Конвертация происходит не в этом методе.
        :param base_curr: Базовая валюта 3 символа в верхнем регистре.
        :param target_curr: Избранная валюта Базовая валюта 3 символа в верхнем регистре.
        :param rate: Текущий курс.
        :param amount: Сколько меняем.
        :param result: Готовый результат обмена.
        :return __dicts_result: Готовый словарь с данными.
        """
        bt_object = BaseTargetClasses()
        __base_currency = bt_object.base_select(base_curr)
        __target_currency = bt_object.target_select(target_curr)
        __dicts_result = {
            'BaseCurrency': __base_currency,
            'TargetCurrency': __target_currency,
            'Rate': rate,
            'Amount': amount,
            'ConvertedAmount': result
        }

        return __dicts_result

    @staticmethod
    def converter_json_string(data_object, code_currency=None):
        """
        Метод конвертирует информацию из запросов
        в json строку и возвращает эту самую строку
        для отображения.
        :param data_object: Принимает на вход словарь c данными.
        :param code_currency: Принимает на вход код валюты.
        :return: json строка/объект
        """
        __decode_data = data_object
        __data_json = json.dumps(__decode_data, sort_keys=False, indent=4, ensure_ascii=False)

        if len(__data_json) <= 2:
            print(f'Информации о валюте {code_currency} в базе данных нет')
            return f'There is no information about the currency {code_currency} in the database'
        else:
            print(__data_json)
            return __data_json
