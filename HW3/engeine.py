from HW3.worker import worker
from CEO import CEO
from Util import saved_commands,k_worker_type,defs


class engeine:

    def __init__(self):
        self.is_a_CEO = False
        self.Organization_tree= []
        self.num_of_employees = 0

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

    def add_worker(self,worker_data,):

        manager = self.find_worker(worker_data[defs.manager_id.name])
        if manager:
            _worker = worker(name=worker_data[defs.name.name],
                      department=worker_data[defs.department.name],
                      age=worker_data[defs.age.name],
                      type=worker_data[defs.type.name],
                      manager_id = worker_data[defs.manager_id.name])

            manager.add_employee(_worker)
        else:
            print(f"{worker_data[defs.manager_id.name]} not found")

    def find_worker(self,id):
        for root in self.Organization_tree:
            worker = root.get_worker_by_id(id)
            if not worker:
                print(f'worker {id} not founde')
        return worker

    def delete_worker(self,id,force = 0):
        worker = self.find_worker(id)
        if not worker:
            return

        if worker.employees and force == 0:
            print("this worker is manager cant remove it")
            return

        worker_manager = self.find_worker(worker.manager_id)
        worker_manager.employees.remove(worker)
        print(f"worker {worker.name} removed sucssessfult")

    def print_worker(self,id):
        worker = self.find_worker(id)
        if worker:
            print(worker.get_detail())

    def asign_manager(self, worker_id, manager_id):
        worker = self.find_worker(worker_id)
        if not worker:
            return

        if worker.manager_id == manager_id:
            print("this worker alredy belong to the manger")
            return

        new_manager = self.find_worker(manager_id)
        if not new_manager:
            return

        self.delete_worker(worker_id,force = 1)
        worker.manager_id = manager_id
        worker.department = new_manager.department
        new_manager.add_employee(worker)
        print(f'worker {worker_id} assined sucssessfully to manager {manager_id}')

    def print_tree(self):
            for root in self.Organization_tree:
                root.print_manager(3)

    def print_dep(self):
        for root in self.Organization_tree:
            for w in root.employees:
                print(f'|- {w.department}')
                w.print_dep_manager()