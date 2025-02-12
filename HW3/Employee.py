import abc
from dataclasses import dataclass



class Employee:

    __id_counter = 1

    def __init__(self,name: str, department: str, age: int ):
        self._name: str = name
        self._department: str = department
        self._age: int = age
        self._employees: list = []
        self._id: int = None
        self._gen_uniq_id()

    def _gen_uniq_id(self) -> None:
        self._id = Employee.__id_counter
        Employee.__id_counter += 1
    def get_detail(self) -> str:
        return (f"name = {self.name}\n"
                f"id = {self.id}\n"
                f"department = {self.department}\n"
                f"age = {self.age}\n"
                f"type = {self.type}\n")
    def asign_employee(self,new_employee) -> None:
        self.employees.append(new_employee)
    def get_worker_by_id(self, id: int):
        if id == self._id:
            return self
        for emp in self.employees:
            worker = emp.get_worker_by_id(id)
            if worker:
                return worker
        return
    def print_worker_for_tree(self,indent:int = 0) -> None:

        print((" "* indent) + f"|---{self.type} | {self.department} | {self.name} - {self.age}")
        if self.employees:
            for emp in self.employees:
                emp.print_worker_for_tree(indent + 2)
        return

    @property
    def name(self):
        return self._name
    @property
    def department(self):
        return self._department
    @department.setter
    def department(self, department: str):
        self._department = department
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age: int):
        self._age = age
    @property
    def employees(self):
        return self._employees
    @property
    def id(self):
        return self._id