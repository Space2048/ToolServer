
class TemplateEngine(object):
    def __init__(self):
        pass

    def render(self,fileDir, params = []):
        file = open(fileDir,"r")
        text = file.read()
        return text