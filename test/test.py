# import platform

# py_version = platform.python_version().split(".")[0]
# print(py_version)


# import threading

# class Communicator(object):
#     _instance_lock = threading.Lock()

#     def __init__(self,):
#         pass
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(Communicator, "_instance"):
#             with Communicator._instance_lock:
#                 if not hasattr(Communicator, "_instance"):
#                     Communicator._instance = object.__new__(cls)  
#         return Communicator._instance

# comm = Communicator()

# import threading
# class Singleton(object):
#     _instance_lock = threading.Lock()

#     def __init__(self):
#         pass

#     def __new__(cls, *args, **kwargs):
#         if not hasattr(Singleton, "_instance"):
#             with Singleton._instance_lock:
#                 if not hasattr(Singleton, "_instance"):
#                     Singleton._instance = object.__new__(cls)  
#         return Singleton._instance

# obj1 = Singleton()
# obj2 = Singleton()
# print(obj1,obj2)

# def task(arg):
#     obj = Singleton()
#     print(obj)

# for i in range(10):
#     t = threading.Thread(target=task,args=[i,])
#     t.start()


