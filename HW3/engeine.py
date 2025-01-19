from HW3.worker import worker
from CEO import CEO
from collections import deque

from worker_type import k_worker_type
class engeine:

    def __init__(self):
        self.is_a_CEO = False
        self.Organization_tree= []


    def add_employee(self,command):

        if command["type"] != 'CEO':
                #new_worker = worker(name=command["name"], department=command["department"], age=command["age"],type=command['type'],manager_id = command['manager_id'])
                for root in self.Organization_tree:
                    manager = root.get_worker_by_id(command['manager_id'])
                if manager:
                    manager.add_employee(worker(name=command["name"], department=command["department"], age=command["age"],type=command['type'],manager_id = command['manager_id']))
                else:
                    print(f"{command['manager_id']} not found")
        elif not self.is_a_CEO:
            self.is_a_CEO = True
            self.Organization_tree.append(CEO(name = command["name"], department = command["department"], age = command["age"] ))
        else:
            print("there is alredy manc")
            return

