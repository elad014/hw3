from worker import worker
from CEO import CEO
from Util import worker_type,args,Util


class Engine:

    def __init__(self):
        self.is_a_CEO = False
        self.Organization_tree= []
        self.departments = {}
        self.num_of_employees = 0

    def add_employee(self,worker_data):

        if worker_data[args.type.name] == worker_type.CEO.name and self.is_a_CEO:
            Util.Logger(msg='CEO is exist cant add another one', type='e')
            return

        if worker_data[args.type.name] == worker_type.CEO.name:
            self.is_a_CEO = True
            self.add_CEO(worker_data)

        else:
            self.add_worker(worker_data)

        Util.Logger(msg='Worker added Successfully', type='i')

    def add_CEO(self,worker_data):
        self.is_a_CEO = True

        ceo = CEO(name=worker_data[args.name.name],
                department=worker_data[args.department.name],
                age=worker_data[args.age.name])

        self.Organization_tree.append(ceo)
        self.add_to_departments_tree(ceo)
        self.num_of_employees += 1
    def add_director(self,director):
        self.Organization_tree.append(director)
        self.add_to_departments_tree(director)

    def add_worker(self,worker_data):

        manager = self.find_worker(worker_data[args.manager_id.name])
        _worker = worker(name=worker_data[args.name.name],
                         department=worker_data[args.department.name],
                         age=worker_data[args.age.name],
                         type=worker_data[args.type.name],
                         manager_id = worker_data[args.manager_id.name])

        manager.add_employee(_worker)
        self.add_to_departments_tree(_worker)
        self.num_of_employees += 1

    def add_to_departments_tree(self,worker):
        if worker.department in self.departments:
            self.departments[worker.department].append(worker)
        else:
            tmp = []
            tmp.append(worker)
            self.departments[worker.department] = tmp

    def find_worker(self,id):
        worker = self.Organization_tree[0].get_worker_by_id(id)
        if worker:
            return worker

    def delete_worker(self,id,assign = False):
        worker = self.find_worker(id)
        manager = self.find_worker(worker.manager_id)
        manager.employees.remove(worker)

        if not assign:
            self.num_of_employees -= 1
            Util.Logger(msg=f"worker {worker.name} removed sucssessfult", type = "i")
        self.departments[worker.department].remove(worker)

    def print_worker(self,id):
        worker = self.find_worker(id)
        if worker:
            print(worker.get_detail())

    def asign_manager(self, worker_id, manager_id):
        worker = self.find_worker(worker_id)
        new_manager = self.find_worker(manager_id)


        self.delete_worker(worker_id,assign = True)
        worker.manager_id = manager_id
        worker.department = new_manager.department
        new_manager.add_employee(worker)
        self.departments[worker.department].append(worker)
        Util.Logger(msg = f'worker {worker_id} assined sucssessfully to manager {manager_id}', type ="i")

    def print_tree(self):
            for root in self.Organization_tree:
                root.print_worker()

    def print_dep(self):
        Util.Logger(msg =f"Total Number of employees = {self.num_of_employees}")
        for department, worker_list in self.departments.items():
            Util.Logger(msg =(" " *2 ) + department + f" | number of employees = {len(worker_list)}")
            for worker in worker_list:
                Util.Logger(msg = (" " * 4) + f"|---{worker.type} | {worker.department} | {worker._id} | {worker.name} - {worker.age}")
