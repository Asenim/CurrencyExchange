import json


class WorkJsonFiles:
    def __init__(self, file):
        """
        Класс принимает на вход файл в который
        нужно записать информацию.
        Сам класс занимается Записью нужной информации в
        json файлы.
        :param file: Файл расширения .json
        """
        self.file = file

    def write_in_files(self, data):
        """
        Метод записывает информацию в файл
        :param data:
        :return:
        """
        # # Сохранение данных в виде json строки
        # data = json.dumps(data)
        # # Загрузка данных в виде json строки
        # data = json.loads(str(data))

        with open(self.file, 'w', encoding='utf-8') as file:
            # Сохраняем данные в файл
            json.dump(data, file, indent=6, ensure_ascii=False)

    def read_in_files(self):
        pass

    @staticmethod
    def output_consolas(data):
        data = json.dumps(data, indent=4)
        # data = json.loads(str(data))
        return data


dumping = {
    'Curse': 'Kevin',
    'Salasy': 'Jenny',
    'Kindred': {
        'id': 1,
        'name': 'Filing',
        'datainf': [1, 2, 3]
    }
}

work = WorkJsonFiles('data_file.json')
work.write_in_files(dumping)
print(work.output_consolas(dumping))