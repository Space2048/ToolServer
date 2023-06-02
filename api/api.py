from webserver.server.Server import Routerv4
from webserver.server.Response import Response

router = Routerv4()

@router.get("/")
def main(request):
    
    res = {}
    res["resCode"] = 200
    res["resType"] = "text/html"
    res["buf"] = str(request.remote_addr) + "  APIMAIN..."
    return res

# main = router.get("/")
#用户登录获取token
def login(request):
    pass
