from HW3.worker import worker
from CEO import CEO
from Util import saved_commands,k_worker_type,defs


class engeine:

    def __init__(self):
        self.is_a_CEO = False
        self.Organization_tree= []


    def add_employee(self,worker_data):

        if worker_data[defs.type.name] != k_worker_type.CEO.name:
            self.add_worker(worker_data)
        elif not self.is_a_CEO:
            self.add_CEO(worker_data)
        else:
            print("there is alredy manc")
            return

    def add_CEO(self,worker_data):
        self.is_a_CEO = True
        self.Organization_tree.append(
            CEO(name=worker_data[defs.name.name],
                department=worker_data[defs.department.name],
                age=worker_data[defs.age.name]))

    def add_worker(self,worker_data):

        manager = self.find_manager(worker_data[defs.manager_id.name])
        if manager:
            _worker = worker(name=worker_data[defs.name.name],
                      department=worker_data[defs.department.name],
                      age=worker_data[defs.age.name],
                      type=worker_data[defs.type.name],
                      manager_id = worker_data[defs.manager_id.name])

            manager.add_employee(_worker)
        else:
            print(f"{worker_data[defs.manager_id.name]} not found")

    def find_manager(self,id):
        for root in self.Organization_tree:
            manager = root.get_worker_by_id(id)
        return manager

    def print_tree(self):
            for root in self.Organization_tree:
                root.print_manager(3)