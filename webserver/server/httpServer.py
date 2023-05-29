from http.server import HTTPServer, BaseHTTPRequestHandler
from HttpRequestManagerx import HttpRequestManagerx
import urllib
 
data = {'result': 'this is a test'}
host = ('localhost', 8888)


class HttpServerHandler(BaseHTTPRequestHandler):
    httpMethodManagerx = HttpRequestManagerx()
    timeout = 5
    server_version = "EathSV"
    def do_GET(self):
        dealObj = HttpServerHandler.httpMethodManagerx
        params = {}
        reqUrl = self.path
        if '?' in self.path:#如果带有参数
            reqUrl = self.path.split('?',1)[0]
            self.queryString = urllib.parse.unquote(self.path.split('?',1)[1])
            params = urllib.parse.parse_qs(self.queryString)
        print(params)
        print(self.command, reqUrl)
        handlerMethod = dealObj.get_method(self.command, reqUrl)
        if not handlerMethod:
            self._default()
            return
        res = handlerMethod()

        self.send_response(res["resCode"])
        self.send_header("Content-type",res["resType"]) #"text/html"
        self.end_headers()
        buf = res["buf"]
        self.wfile.write(buf.encode("utf-8"))

    def do_POST(self):
        path = self.path
        print(path)
        #获取post提交的数据
        datas = self.rfile.read(int(self.headers['content-length']))    #固定格式，获取表单提交的数据
        #datas = urllib.unquote(datas).decode("utf-8", 'ignore')
        self.send_response(200)
        self.send_header("Content-type","text/html")    #设置post时服务器的响应头
        self.send_header("test","This is post!")
        self.end_headers()
 
        html = '''<!DOCTYPE HTML>
        <html>
            <head>
                <title>Post page</title>  
            </head>
            <body>
                Post Data:%s  <br />
                Path:%s
            </body>
        </html>''' %(datas,self.path)
        self.wfile.write(html.encode())  #提交post数据时，服务器跳转并展示的页面内容
    
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


# class RequestAspect():
#     def __init__(self):
#         pass
# def test():
#     # httpServerHandler = HttpServerHandler()
#     # print(vars(httpServerHandler))
#     #host="127.0.0.1"
#     httpMethodManager = HttpRequestManagerx()
    
#     httpMethodManager.add_url_method("/userName", getUserName)
#     httpMethodManager.add_url_method("/", default)
    
#     server = HTTPServer(host, HttpServerHandler)

#     print("Starting server, listen at: %s:%s" % host)
#     server.serve_forever()

# test()