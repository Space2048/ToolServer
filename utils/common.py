from utils import globalvb as gbv
import time
from loguru import logger
import yaml
from yaml.loader import SafeLoader
import json
import os

class obj(object):
    def __init__(self, dict_):
        self.__dict__.update(dict_)

def dictToObj(d):
    return json.loads(json.dumps(d), object_hook=obj)

def loadConfig():
    with open('./config/default.yaml') as f:
        data = yaml.load(f, Loader = SafeLoader)
        gbv.set_value("config", data)

def initLog():
    logger.add("./logs/toolcenter_log_{time}.log", encoding="utf-8", enqueue=True, rotation="500MB", compression="zip", retention="10 days")
    logger.info("initLog...")

def getConfig(name):
    data = gbv.get_value("config")
    logger.info(data)
    return dictToObj(data[name])