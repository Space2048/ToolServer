#run app
from view import create_app
from utils import globalvb as gbv
from utils import common
from loguru import logger
if __name__ == '__main__':
    app = create_app()
    #创建全局变量
    gbv._init()
    #加载配置
    common.loadConfig()
    server = common.getConfig("server")
    host = server.host
    port = server.port
    #初始化日志
    common.initLog()
    logger.info("start " + host + " " + str(port))
    app.run(host=host, port=port)