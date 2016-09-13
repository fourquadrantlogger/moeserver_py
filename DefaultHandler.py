from http.server import BaseHTTPRequestHandler

import HttpRequest
import HttpResponse


class DefaultHandler(BaseHTTPRequestHandler):
    def Get(self,req=HttpRequest,resp=HttpResponse):
        resp.code(404).close()

    def POST(self,req=HttpRequest,resp=HttpResponse):
        resp.code(404).close()

    def PUT(self,req=HttpRequest,resp=HttpResponse):
        resp.code(404).close()

    def DELETE(self,req=HttpRequest,resp=HttpResponse):
        resp.code(404).close()

    def TRACE(self,req=HttpRequest,resp=HttpResponse):
        resp.code(404).close()

    def HEAD(self,req=HttpRequest,resp=HttpResponse):
        resp.code(404).close()
