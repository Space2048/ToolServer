from http.server import HTTPServer
from httpServer import HttpServerHandler
from HttpRequestManagerx import HttpRequestManagerx


class Server:
    def __init__(self, name, host = "localhost", v4Port = 80, v6Port = 8080,sPort = 9090):
        self.name = name
        self.host = host
        self.v4Port = v4Port
        self.v6Port = v6Port
        self.sPort = sPort
        self.httpReqMgr = HttpRequestManagerx()
    
    def run(self):
        v4host = (self.host, self.v4Port)
        server = HTTPServer(v4host, HttpServerHandler)
        server.serve_forever()

    def registerv4Method(self, rtype, router, func):
        return self.httpReqMgr.add_url_method(rtype, router, func)



#---------------------------------------controler-------------------------------------------
def getUserName():
    res = {}
    res["resCode"] = 200
    res["resType"] = "text/html"
    res["buf"] = "getUserName"
    return res

def default():
    res = {}
    res["resCode"] = 200
    res["resType"] = "text/html"
    res["buf"] = "default"
    return res
#------------------------------------end---------------------------------------------------

def test():
    server = Server("gs1", v4Port= 8081)
    server.registerv4Method("GET","/getUserName", getUserName)
    server.registerv4Method("GET", "/", default)
    server.run()

test()