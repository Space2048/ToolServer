from http.server import HTTPServer
from webserver.server.httpServer import HttpServerHandler
from webserver.server.HttpRequestManagerx import HttpRequestManagerx
from webserver.server.Supervise import ConnectCenter

from types import FunctionType

class Server():
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
        #connectCenter = ConnectCenter()
        #ConnectCenter.run()
        server.serve_forever()

    def registerV4Router(self, routerv4):
        self.routerV4 = routerv4

    def registerv4Method(self, rtype, router, func):
        return self.httpReqMgr.add_url_method(rtype, router, func)

class Routerv4(object):

    httpMgrV4 = HttpRequestManagerx()

    def get(self, path):
        def decorator(func: FunctionType):
            self._register(rType = "GET", router = path, func = func)
        return decorator

    def post(self, path):
        def decorator(func: FunctionType):
            self._register(rType = "POST", router = path, func = func)
        return decorator

    def _register(self, rType, router, func):
        httpMgr = HttpRequestManagerx()
        httpMgr.add_url_method(rType, router,func)

#---------------------------------------controler-------------------------------------------

def getUserName(request):
    res = {}
    res["resCode"] = 200
    res["resType"] = "text/html"
    res["buf"] = "getUserName"
    return res

def default(request):
    res = {}
    res["resCode"] = 200
    res["resType"] = "text/html"
    res["buf"] = getGepJs()
    return res

def setUserPosition(request):
    res = {}
    res["resCode"] = 200
    res["resType"] = "text/html"
    res["buf"] = request.client_address
    return res

def getGepJs():
    h5File = open("../temp/test.html","r")
    text = h5File.read()
    h5File.close()
    return text

def setError(request):
    res = {}
    res["resCode"] = 200
    res["resType"] = "text/html"
    res["buf"] = str(request.remote_addr)
    return res

#------------------------------------end---------------------------------------------------
#------------test
# routerd = routerv4()

# @routerd.get("/")
# def main(request):
#     res = {}
#     res["resCode"] = 200
#     res["resType"] = "text/html"
#     res["buf"] = str(request.remote_addr) + "  MAIN..."
#     return res

#------------end

def test():
    server = Server("gs1", host="localhost", v4Port= 8081)

    #server.registerV4Router(router)
    #server.registerv4Method("GET","/getUserName", getUserName)
    #server.registerv4Method("GET", "/", default)
    #server.registerv4Method("POST", "/setUserPosition", setUserPosition)
    #server.registerv4Method("POST", "/setPositionError", setError)
    server.run()

#test()