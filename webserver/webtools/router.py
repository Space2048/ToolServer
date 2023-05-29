from functools import wraps


class Router():
    def __init__(self) -> None:
        pass

    def __call__(self, func, method, path):
        def decorator(func, method, path):
            pass
