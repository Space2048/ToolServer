from  utils.designpattern import singletonMeta

class RequestAspect(metaclass= singletonMeta):
    
    def __init__(self):
        RequestAspect.ruleLib = {}
        pass
    def registerRule(rule, func):
        pass
