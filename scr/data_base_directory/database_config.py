import sqlite3
import json


def output_data_in_json(cursor):
    """
    Выводит данные из базы данных в консоль
    переводя их в json объект
    :param cursor: Параметр позволяет общаться с базой данных
        и делать запросы, принимает на вход метод cursor класса
        sqlite3
    :return data_json: Возвращает, данные в формате json
    """
    data = cursor.execute('SELECT * FROM Currencies;')
    data_json = json.dumps(data.fetchall(), ensure_ascii=False, indent=4)
    # data_json = json.loads(str(data_json))
    return data_json


def write_data_in_json(file, cursor):
    data = cursor.execute('SELECT * FROM Currencies;')
    data_json = json.dumps(data.fetchall(), indent=4)
    data_json = json.loads(str(data_json))
    with open(file, 'w', encoding='utf-8') as file:
        json.dump(data_json, file, indent=4)


data_base = sqlite3.connect("admin_db.db")
request = data_base.cursor()

print(output_data_in_json(request))
write_data_in_json('data_file.json', request)

request.close()
data_base.close()
