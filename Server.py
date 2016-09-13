from http.server import HTTPServer, BaseHTTPRequestHandler

class Server:
    def __init__(self):
        self.server=HTTPServer
        self.port=8000
        self.default_handler=BaseHTTPRequestHandler

    def setport(self,Port):
        self.port=Port
    def run(self):
        server_address = ('', self.port)
        httpd = HTTPServer(server_address, self.default_handler)
        self.default_handler.