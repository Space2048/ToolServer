from utils import singletonMeta

class HttpRequestManagerx(metaclass=singletonMeta):
    _methodLib = {}
    
    #初始化请求管理器
    def __init__(self):
        if not HttpRequestManagerx._methodLib:
            HttpRequestManagerx._methodLib = {}
            methodMap = HttpRequestManagerx._methodLib
            methodMap["GET"] = {}
            methodMap["POST"] = {}
            methodMap["HEAD"] = {}
            methodMap["OPTIONS"] = {}
            methodMap["PUT"] = {}
            methodMap["PATCH"] = {}
            methodMap["DELETE"] = {}
            methodMap["TRACE"] = {}
            methodMap["CONNECT"] = {}
    
    #存储方法
    def add_url_method(self, rtype, url, method):
        HttpRequestManagerx._methodLib[rtype][url] = method

    #根据url获取请求方法
    def get_method(self, rtype, url):
        if not url in HttpRequestManagerx._methodLib[rtype].keys():
            return
        method = HttpRequestManagerx._methodLib[rtype][url]
        return method
    
