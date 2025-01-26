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
        self.num_of_employees = 0
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
                f"type = {self.type}\n")

    def get_id(self):
        return self._id

    def add_employee(self,new_employee):
        print(f"{new_employee.name} added {new_employee._id}")
        self.employees.append(new_employee)

    def get_worker_by_id(self, id):
        if id == self._id:
            return self
        for emp in self.employees:
            worker = emp.get_worker_by_id(id)
            if worker:
                return worker
        return

    def print_manager(self,indent = 3):
        if not self.employees:
            print(("-"* indent) + f"employee: {self.name} {self._id}")
            return
        else:
            print(("-"* indent) + f"manager: {self.name} {self._id}")
            for emp in self.employees:
                emp.print_manager(indent + 2)
        return

    def print_dep_manager(self,indent = 3):
        print(f'|--- {self.name}')
        for emp in self.employees:
            emp.print_dep_manager(indent)
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





