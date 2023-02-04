import logging
from http.server import BaseHTTPRequestHandler, HTTPServer
from src.currencies_request_package.Get_Package.Get_Output_Consolas_Currencies \
    import GetOutputCurrencies
from src.currencies_request_package.Post_Package.Post_Consolas_Currencies import PostConsolasCurrencies
from src.currencies_request_package.Delete_Package.Delete_Consolas_Currensies import DeleteConsolasCurrencies
from src.exchange_rates_request_package.Get_Package.Get_Output_Consolas_Exchange_Rates \
    import GetOutputExchangeRates


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
        if self.path.startswith('/get/currencies/'):
            self.wfile.write(bytes(get_currencies.get_specific(self.path[-3:]), 'utf-8'))

        # Все валюты
        elif self.path.startswith('/get/currencies'):
            self.wfile.write(bytes(get_currencies.get_all(), 'utf-8'))

        # Exchange Rates
        # Конкретный курс
        elif self.path.startswith('/get/exchange/'):
            self.wfile.write(bytes(get_exchange_rates.get_specific(self.path[-6:]), 'utf-8'))

        # Все курсы
        elif self.path.startswith('/get/exchange'):
            self.wfile.write(bytes(get_exchange_rates.get_all(), 'utf-8'))

    def do_POST(self):

        self.send_response(200)
        self.send_header("Content-type", "application/x-www-form-urlencoded")
        body_request = (self.rfile.read(int(self.headers['Content-Length'])))
        self.end_headers()

        post_currencies = PostConsolasCurrencies()

        # Запрос на добавление валюты в базу данных
        if self.path.startswith('/post/currencies'):
            list_body_request = body_request.decode('utf-8').split('&')
            print(list_body_request)
            logging.info('Пост запрос принят успешно')
            self.wfile.write(bytes(post_currencies.post_information(list_body_request[0],
                                                                    list_body_request[1],
                                                                    list_body_request[2]),'utf-8'))

    def do_DELETE(self):

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        delete_currencies = DeleteConsolasCurrencies()

        # Запрос на удаление конкретной валюты из базы данных
        if self.path.startswith('/delete/currencies/'):
            self.wfile.write(bytes(delete_currencies.delete_information(self.path[-3:]), 'utf-8'))


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
