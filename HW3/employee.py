import abc
from dataclasses import dataclass



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
        self.employees.append(new_employee)

    def get_worker_by_id(self, id):
        if id == self._id:
            return self
        for emp in self.employees:
            worker = emp.get_worker_by_id(id)
            if worker:
                return worker
        return

    def print_worker(self,indent = 0):

        print((" "* indent) + f"|---{self.type} | {self.department} | {self.name} - {self.age}")
        if self.employees:
            for emp in self.employees:
                emp.print_worker(indent + 2)
        return

