from http.server import HTTPServer, SimpleHTTPRequestHandler

class NoCacheHTTPHandler(SimpleHTTPRequestHandler):
    def send_response_only(self, code, message=None):
        super().send_response_only(code, message)
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Pragma', 'no-cache')

def run(server_class=HTTPServer, handler_class=NoCacheHTTPHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print('Сервер запущен на http://localhost:8000/')
    httpd.serve_forever()

if __name__ == '__main__':
    run()