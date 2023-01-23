import sqlite3
from scr.abstract_requests_classes.Abstract_Get_Requests import AbstractGetRequests


class GetOutputExchangeRates(AbstractGetRequests):
    def __init__(self, path_data_base=None):

        super().__init__(path_data_base)

    def get_all(self):

        # Происходит подключение к базе данных
        __data_base = sqlite3.connect(self._path_db)
        __cursor = __data_base.cursor()

        # Создается запрос
        __all_data = __cursor.execute(f"""
            SELECT E.ID, C.Code, C2.Code, Rate 
            FROM ExchangeRates E
            JOIN Currencies C on E.BaseCurrencyID = C.ID
            JOIN Currencies C2 on E.TargetCurrencyID = C2.ID;
        """)
        self._converter_json_string(__all_data)

        # Закрываем базу данных
        __cursor.close()
        __data_base.close()

    def get_specific(self, code_currency):

        __data_base = sqlite3.connect(self._path_db)
        __cursor = __data_base.cursor()

        specific_currency = __cursor.execute(f"""
            SELECT E.ID, C.Code, C2.Code, Rate 
            FROM ExchangeRates E
            JOIN Currencies C on E.BaseCurrencyID = C.ID
            JOIN Currencies C2 on E.TargetCurrencyID = C2.ID
            WHERE C.Code = ? and C2.Code = ?
        """, (code_currency[0:3], code_currency[3:]))
        self._converter_json_string(specific_currency)

        __cursor.close()
        __data_base.close()


def test_class():
    path = 'C:/ArhitectFiles/PythonProjects/CurrencyExchange/scr/data_base_directory/admin_db.db'
    db_admin = GetOutputExchangeRates(path)
    db_admin.get_all()
    db_admin.get_specific('USDEUR')


if __name__ == "__main__":
    test_class()
