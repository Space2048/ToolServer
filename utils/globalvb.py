#全局变量库
def _init():
    global _global_dict
    _global_dict = {}

def set_value(key, value):
    if key in _global_dict:
        return False
    _global_dict[key] = value

def get_value(key):
    if key in _global_dict:
        return _global_dict[key]
    return False
    
def existKey(key):
    if key in _global_dict:
        return True
    else:
        return False