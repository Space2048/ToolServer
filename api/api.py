from webserver.server.Server import Routerv4
from webserver.server.Response import Response
from webserver.server.TemplateEngine import TemplateEngine

router = Routerv4()

@router.get("/")
def main(request):
    tme = TemplateEngine()
    return Response(tme.render("/root/toolcenter/webserver/temp/index.html"))

# main = router.get("/")
#用户登录获取token
def login(request):
    pass
