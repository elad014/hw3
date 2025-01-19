import abc
from dataclasses import dataclass

class Util():

    uniq_id = 0

    @staticmethod
    def gen_uniq_id():
        Util.uniq_id += 1
        return Util.uniq_id

class employee:

    id_counter = 1

    def __init__(self,name: str, department: str, age: int ):
        self.name: str = name
        self.department: str = department
        self.age: int = age
        self.employees = []
        self._id = None
        self.gen_uniq_id()

    def gen_uniq_id(self):
        self._id = employee.id_counter
        employee.id_counter += 1


    def get_detail(self):
        return (f"name = {self.name}\n"
                f"id = {self.get_id()}\n"
                f"department = {self.department}\n"
                f"age = {self.age}\n"
                f"type = {self.type}")

    def get_id(self):
        return self._id

    def add_employee(self,new_employee):
        self.employees.append(new_employee)

    def serch_manager(self,id):
        if id == self.get_id():
            return self
        for emp in self.employees:
            res = emp.serch_manager(id)
            return res

    def print_manager(self,space):
        if not self.employees:
            print(("-"* space) + f"employee: {self.name}")
            return
        else:
            print(("-"* space) + f"manager: {self.name}")
            for emp in self.employees:
                emp.print_manager(space + 2)
        return
"""
@dataclass
class employee:

    name: str
    department: str
    age: int
    type: str

    #Util.get_uniq_id()

"""





