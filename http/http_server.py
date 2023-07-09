from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import json

class HttpGetHandler(BaseHTTPRequestHandler):
    """Обработчик с реализованным методом do_GET."""

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        length = int(self.headers.get('Content-length', 0))
        # data = json.loads(self.rfile.read(length).decode())
        # data = json.loads({'message': 'this is data'})
        data = {'message': 'this is data'}

        self.wfile.write(json.dumps(data).encode())

        # self.wfile.write('<html><head><meta charset="utf-8">'.encode())
        # self.wfile.write('<title>Простой HTTP-сервер.</title></head>'.encode())
        # self.wfile.write('<body>Был получен GET-запрос.</body></html>'.encode())


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    port = 8000
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
        print(f'server started at {port}')
    except KeyboardInterrupt:
        httpd.server_close()
        print('server stopped')

if __name__ == '__main__':
    raise SystemExit(run(handler_class=HttpGetHandler))
