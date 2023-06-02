
def defaultHtml():
    return ''

'''
status_code 返回消息状态码
res_type 返回消息类型
res_content 返回消息内容
'''
class Response(object):
    def __init__(self,resContet, code = 200, header = {"Content-type":"text/html"}):
        self._status_code = code
        self._headerMap = header
        if resContet:
            self._res_content = resContet
        else:
            self._res_content = Response.defaultHtml()

    def defaultHtml():
        return ''

    @property
    def status_code(self):
        return self._status_code
    
    @status_code.setter
    def status_code(self, code):
        self._status_code = code

    @property
    def headers(self):
        return self._headerMap
    
    @headers.setter
    def res_type(self, headers):
        self._headerMap = headers
    
    @property
    def res_content(self):
        return self._res_content
    
    @res_type.setter
    def res_content(self, content):
        self.res_content = content
    
    
    
        