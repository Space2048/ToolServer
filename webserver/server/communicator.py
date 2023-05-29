import threading

class Communicator(object):
    _instance_lock = threading.Lock()

    def __init__(self):

        pass
    
    def __new__(cls, *args, **kwargs):
        if not hasattr(Communicator, "_instance"):
            with Communicator._instance_lock:
                if not hasattr(Communicator, "_instance"):
                    Communicator._instance = object.__new__(cls)  
        return Communicator._instance

    # def 
    