from Employee import Employee


class CEO(Employee):

    def __init__(self, name: str, department: str, age: int):
        self._type = "CEO"
        super().__init__(name = name, department = department, age = age)

    @property
    def type(self):
        return self._type