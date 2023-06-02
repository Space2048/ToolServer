from webserver.server.utils import singletonMeta
import threading
import time

class NodeInfo(object):
    def __init__(self, ip, port, timein):
        self._ip = ip
        self._port = port
        self._timein = timein
    @property
    def ip(self):
        return self._ip
    
    @property
    def port(self):
        return self._port
    
    @property
    def timein(self):
        return self._timein

class ConnectCenter(metaclass= singletonMeta):
    _nodeInfoLib = {}
    _ruleMethod = []
    _blockNode = {}

    def __init__(self):
        if not ConnectCenter._nodeInfoLib:
            ConnectCenter._nodeInfoLib = {}
    
    def registerNode(node: NodeInfo):
        if not ConnectCenter._nodeInfoLib:
            ConnectCenter._nodeInfoLib = {}
        if node.ip in ConnectCenter._blockNode.keys():
            return False
        ConnectCenter._nodeInfoLib[node.ip] = node
        return True
    
    def nodeInfoLibData(self):
        return ConnectCenter._nodeInfoLib

    def registerRule(func):
        if not ConnectCenter._ruleMethod:
            ConnectCenter._ruleMethod = []
        ConnectCenter._ruleMethod.append(func)
    
    def fresh():
        if not ConnectCenter._nodeInfoLib:
            ConnectCenter._nodeInfoLib = {}
        if not ConnectCenter._ruleMethod:
            ConnectCenter._ruleMethod = []

        while True:
            for nodeIp in ConnectCenter._nodeInfoLib.keys():
                nodeInfo = ConnectCenter._nodeInfoLib[nodeIp]
                for func in ConnectCenter._ruleMethod:
                    if func(nodeInfo): #被筛到
                        if not ConnectCenter._blockNode:
                            ConnectCenter._blockNode = {}
                        ConnectCenter._blockNode[nodeIp] = nodeInfo
            time.sleep(10)

    def canReq(ip):
        for bip in ConnectCenter._blockNode.keys():
            if bip == ip:
                return False
            return True  

    def run():

        thread = threading.Thread(target=ConnectCenter.fresh())
        thread.start()