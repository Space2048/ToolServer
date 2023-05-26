from http.server import HTTPServer, BaseHTTPRequestHandler
 
data = {'result': 'this is a test'}
host = ('localhost', 8888)


class HttpServerHandler(BaseHTTPRequestHandler):
    timeout = 5
    server_version = "EathSV"
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()
        buf = '''<!DOCTYPE HTML>
                <html>
                    <head>
                        <title>Get page</title>
                    </head>
                <body>
                    <form action="post_page" method="post">
                        username: <input type="text" name="username" /><br />
                        password: <input type="text" name="password" /><br />
                        <input type="submit" value="POST" />
                    </form>
                </body>
                </html>'''
        self.wfile.write(buf.encode())

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

def test():
    httpServerHandler = HttpServerHandler()
    print(vars(httpServerHandler))
    #host="127.0.0.1"
    
    server = HTTPServer(host, HttpServerHandler)

    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()

test()