from scr.abstract_requests_classes.Abstract_Requests import AbstractRequests


class AbstractPostRequests(AbstractRequests):

    def __init__(self):

        super().__init__()

    def post_information(self, arg1, arg2, arg3):
        """
        Данный метод добавляет в базу данных информацию
        по заданным аргументам, в зависимости от таблицы
        содержание и тип аргументов может сильно различаться
        Поэтому в данном классе не будет описания аргументов
        P.S. ID в таблице назначается - автоматически.
        """
        pass
