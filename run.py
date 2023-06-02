#run app
#from view import create_app
#from utils import globalvb as gbv
# from utils import common
# from loguru import logger
from webserver.server.Server import Server
from api.api import router

if __name__ == '__main__':
    # app = create_app()
    # #创建全局变量
    # gbv._init()
    # #加载配置
    # common.loadConfig()
    # server = common.getConfig("server")
    # host = server.host
    # port = server.port
    # #初始化日志
    # common.initLog()
    # logger.info("start " + host + " " + str(port))
    # app.run(host=host, port=port)
    server = Server("gs1", host="localhost", v4Port= 8081)
    server.registerV4Router(router)
    server.run()
