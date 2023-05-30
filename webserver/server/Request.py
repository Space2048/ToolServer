
class Request(object):
    def __init__(self, handerObj):
        self.remote_addr = handerObj.client_address
        self.url_param = handerObj.url_param
        self.headers = handerObj.headers
        self.path = handerObj.path
        pass