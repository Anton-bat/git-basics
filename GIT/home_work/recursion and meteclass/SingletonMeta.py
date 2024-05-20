from typing import Any


class SingletonMeta(type):
    _instance = {}
    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls._instance:
            cls._instance[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instance[cls]\
        
class Singleton(metaclass=SingletonMeta):
    def something(self):
        pass
if __name__ == "__main__":

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")
