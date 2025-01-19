from employee import *

class MetaCEO(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class CEO(employee,metaclass=MetaCEO):

    def __init__(self, name: str, department: str, age: int):
        self.test = 1
        self.type = "CEO"
        super().__init__(name = name, department = department, age = age)

