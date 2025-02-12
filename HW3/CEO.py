from employee import *


class CEO(employee):

    def __init__(self, name: str, department: str, age: int):
        self.type = "CEO"
        super().__init__(name = name, department = department, age = age)

