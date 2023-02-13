import logging
from http.server import BaseHTTPRequestHandler, HTTPServer
from src.currencies_request_package.Request_Methods import *
from src.exchange_rates_request_package.Request_Methods import *


class HandlerServer(BaseHTTPRequestHandler):

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s; %(levelname)s; '
               '%(module)s; %(lineno)s; '
               '%(funcName)s; %(message)s'
    )
    logging.getLogger(__name__)

    def do_GET(self):

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        get_currencies = GetOutputCurrencies()
        get_exchange_rates = GetOutputExchangeRates()

        # Currencies
        # Конкретная валюта
        if self.path.startswith('/currencies/'):
            self.wfile.write(bytes(get_currencies.get_specific(self.path[-3:]), 'utf-8'))

        # Все валюты
        elif self.path.startswith('/currencies'):
            self.wfile.write(bytes(get_currencies.get_all(), 'utf-8'))

        # Exchange Rates
        # Конкретный курс
        elif self.path.startswith('/exchange/'):
            self.wfile.write(bytes(get_exchange_rates.get_specific(self.path[-6:]), 'utf-8'))

        # Все курсы
        elif self.path.startswith('/exchange'):
            self.wfile.write(bytes(get_exchange_rates.get_all(), 'utf-8'))

    def do_POST(self):

        self.send_response(200)
        self.send_header("Content-type", "application/x-www-form-urlencoded")
        body_request = (self.rfile.read(int(self.headers['Content-Length'])))
        self.end_headers()

        post_currencies = PostConsolasCurrencies()
        post_exchange_rates = PostConsolasExchangeRates()

        # Currency
        # Запрос на добавление валюты в базу данных
        if self.path.startswith('/currencies'):
            list_body_request = body_request.decode('utf-8').split('&')
            print(list_body_request)
            logging.info('Пост запрос принят успешно')
            self.wfile.write(bytes(post_currencies.post_information(list_body_request[0],
                                                                    list_body_request[1],
                                                                    list_body_request[2]), 'utf-8'))

        # Exchange rates
        if self.path.startswith('/exchange'):
            list_body_request = body_request.decode('utf-8').split('&')
            print(list_body_request)
            logging.info('Пост запрос принят успешно')
            self.wfile.write(bytes(post_exchange_rates.post_information(list_body_request[0],
                                                                        list_body_request[1],
                                                                        list_body_request[2]), 'utf-8'))

    def do_PATCH(self):

        self.send_response(200)
        self.send_header("Content-type", "application/x-www-form-urlencoded")
        body_request = (self.rfile.read(int(self.headers['Content-Length'])))
        self.end_headers()

        patch_exchange_rates = PatchConsolasExchangeRates()

        # Запрос на изменение курса валюты
        if self.path.startswith('/exchange/'):
            list_body_request = body_request.decode('utf-8').split('&')
            print(list_body_request)
            logging.info('Патч запрос принят успешно')
            self.wfile.write(bytes(patch_exchange_rates.change_column(self.path[-6:],
                                                                      list_body_request[0]), 'utf-8'))

    def do_DELETE(self):

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        delete_currencies = DeleteConsolasCurrencies()
        delete_exchange = DeleteConsolasExchangeRates()

        # Currency
        # Запрос на удаление конкретной валюты из базы данных
        if self.path.startswith('/currencies/'):
            self.wfile.write(bytes(delete_currencies.delete_information(self.path[-3:]), 'utf-8'))

        # ExchangeRates
        if self.path.startswith('/exchange/'):
            self.wfile.write(bytes(delete_exchange.delete_information(self.path[-6:]), 'utf-8'))


if __name__ == "__main__":
    hostName = "localhost"
    serverPort = 7080

    webServer = HTTPServer((hostName, serverPort), HandlerServer)
    print("Сервер запущен http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Сервер остановлен.")
