from http.server import HTTPServer, BaseHTTPRequestHandler
from webserver.server.HttpRequestManagerx import HttpRequestManagerx
from webserver.server.Request import Request
from webserver.server.Response import Response
from webserver.server.Supervise import ConnectCenter, NodeInfo
import time
import urllib


class HttpServerHandler(BaseHTTPRequestHandler):
    httpMethodManagerx = HttpRequestManagerx()
    timeout = 5
    server_version = "EathSV"
    def do_GET(self):
        # if not self._registerConnect(self.client_address):
        #     self._default()
        #     return

        dealObj = HttpServerHandler.httpMethodManagerx
        params = {}
        reqUrl = self.path
        print(reqUrl)
        if '?' in self.path:#如果带有参数
            reqUrl = self.path.split('?',1)[0]
            self.queryString = urllib.parse.unquote(self.path.split('?',1)[1])
            params = urllib.parse.parse_qs(self.queryString)
        self.url_param = params
        request = Request(self)
        handlerMethod = dealObj.get_method(self.command, reqUrl)
        if not handlerMethod:
            self._default()
            return
        res: Response = handlerMethod(request)
        self.send_response(res.status_code)
        self.send_header("Content-type",res["resType"]) #"text/html"
        self.end_headers()
        buf = res.res_content
        self.wfile.write(buf.encode("utf-8"))

    def do_POST(self):
        # if not self._registerConnect(self.client_address):
        #     self._default()
        #     return
        dealObj = HttpServerHandler.httpMethodManagerx
        params = {}
        reqUrl = self.path
        self.url_param = params
        req_datas = self.rfile.read(int(self.headers['content-length']))
        self.req_datas = req_datas
        request = Request(self)
        handlerMethod = dealObj.get_method(self.command, reqUrl)
        if not handlerMethod:
            self._default()
            return
        res = handlerMethod(request)
        self.send_response(res["resCode"])
        self.send_header("Content-type",res["resType"]) #"text/html"
        self.end_headers()
        buf = res["buf"]
        self.wfile.write(buf.encode("utf-8"))
    
    def _dispatchReq(self):
        # if not self._registerConnect(self.client_address):
        #     self._default()
        #     return
        dealObj = HttpServerHandler.httpMethodManagerx
        reqUrl = self.path
        params = {}
        print(reqUrl)
        if '?' in self.path:#如果带有参数
            reqUrl = self.path.split('?',1)[0]
            self.queryString = urllib.parse.unquote(self.path.split('?',1)[1])
            params = urllib.parse.parse_qs(self.queryString)
        self.url_param = params
        req_datas = self.rfile.read(int(self.headers['content-length']))
        self.req_datas = req_datas
        request = Request(self)
        handlerMethod = dealObj.get_method(self.command, reqUrl)
        if not handlerMethod:
            self._default()
            return
        res: Response = handlerMethod(request)
        self.send_response(res.status_code)
        for headerK in res.headerMap.keys():
            value = res.headerMap[value]
            self.send_header(headerK, value)
        self.end_headers()
        buf = res.res_content
        self.wfile.write(buf.encode("utf-8"))



    def _default(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()
        buf = '''<!DOCTYPE html>
            <html>
            <head>
            </head>
            <body>
            <h1>b_server fail</h1>
            </body>
            </html>'''
        self.wfile.write(buf.encode("utf-8"))

    def _registerConnect(self, client_address):
        nodeInfo = NodeInfo(client_address[0], client_address[1], int(time.time()))
        connectCenter = ConnectCenter()
        if connectCenter.registerNode(nodeInfo):
            if connectCenter.canReq(nodeInfo.ip):
                return True
        return False
