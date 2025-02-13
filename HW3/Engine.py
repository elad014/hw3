from Worker import Worker
from CEO import CEO
from Util import Util
from Defs import worker_type,args


class Engine:

    def __init__(self):
        self._is_a_CEO = False
        self._organization_tree= []
        self._departments = {}
        self._num_of_employees = 0
    def add_employee(self,worker_data: dict) -> None:
        """
        this func get worker data and checks if to creat worker or ceo object
        :param worker_data dict:
        :return: none
        """
        if worker_data[args.type.name] == worker_type.CEO.name and self._is_a_CEO:
            Util.Logger(msg='CEO is exist cant add another one', type='e')
            return

        if worker_data[args.type.name] == worker_type.CEO.name:
            self._is_a_CEO = True
            self._add_CEO(worker_data = worker_data)
        else:
            self._add_worker( worker_data = worker_data)

        Util.Logger(msg='Worker added Successfully', type='i')

    def find_worker(self,id: int) -> Worker:
        """
        this function get worker id and call the ceo to search inside heas employees
        :param id:
        :return: worker or none
        """
        worker = self._organization_tree[0].get_worker_by_id(id = id)
        if worker:
            return worker

    def delete_worker(self,id: int ,assign: bool = False) -> None:
        """
        get worker id and find his manager and remove it from the employyees of the manager
        it hendel also the department database
        assine true: is flag that use by assinee_manager (if assign dont print and dont change the number of employees)
        :param id:
        :param assign:
        :return: None
        """
        worker = self.find_worker(id = id)
        manager = self.find_worker(id = worker.manager_id)
        manager.employees.remove(worker)

        if not assign:
            self._num_of_employees -= 1
            Util.Logger(msg=f"worker {worker.name} removed sucssessfult", type = "i")
        self._departments[worker.department].remove(worker)
    def print_tree(self) -> None:
        """
        call for the ceo and active recursive func that print rach employee
        :return:
        """
        for root in self._organization_tree:
            root.print_worker_for_tree()

    def print_worker(self,id: int) -> None:
        """
        get id worker finede him and print his details
        :param id:
        :return:
        """
        worker = self.find_worker(id = id)
        if worker:
            Util.Logger(msg = worker.get_detail())
    def asign_manager(self, worker_id: int, manager_id: int) -> None:
        """
        this func get worker id and manager
        remove the worker from old manager
        change worker department to the new manager department
        and add the worker to the new manager
        :param worker_id:
        :param manager_id:
        :return:
        """
        worker = self.find_worker(id = worker_id)
        new_manager = self.find_worker(id = manager_id)
        self.delete_worker(id = worker_id,assign = True)
        worker.manager_id = manager_id
        worker.department = new_manager.department
        new_manager.asign_employee(worker)
        self._departments[worker.department].append(worker)
        Util.Logger(msg = f'worker {worker_id} assined sucssessfully to manager {manager_id}', type ="i")
    def print_dep(self) -> None:
        """
        print the department database
        :return:
        """
        Util.Logger(msg =f"Total Number of employees = {self._num_of_employees}")
        for department, worker_list in self._departments.items():
            Util.Logger(msg =(" " *2 ) + department + f" | number of employees = {len(worker_list)}")
            for worker in worker_list:
                Util.Logger(msg = (" " * 4) + f"|---{worker.type} | {worker.department} | {worker._id} | {worker.name} - {worker.age}")
        

    def _add_CEO(self,worker_data: dict) -> None:
        """
        this func create coe object and add him to organization tree and to the department
        :param worker_data:
        :return:
        """
        self.is_a_CEO = True
        ceo = CEO(name=worker_data[args.name.name],
                department=worker_data[args.department.name],
                age=worker_data[args.age.name])

        self._organization_tree.append(ceo)
        self._add_to_departments_tree(worker = ceo)
        self._num_of_employees += 1
    def _add_worker(self,worker_data: dict):
        """
        this func get the worker data crate worker object and add hit to the manager
        and add him to rhw department database
        :param worker_data:
        :return:
        """
        manager = self.find_worker(id = worker_data[args.manager_id.name])
        new_worker = Worker(name=worker_data[args.name.name],
                         department=worker_data[args.department.name],
                         age=worker_data[args.age.name],
                         type=worker_data[args.type.name],
                         manager_id = worker_data[args.manager_id.name])

        manager.asign_employee(new_worker)
        self._add_to_departments_tree(worker = new_worker)
        self._num_of_employees += 1
    def _add_to_departments_tree(self,worker: Worker):
        """
        this func update departments in department database
        if the department wxist add the worker to the department if no create new department in case is a director
        :param worker:
        :return:
        """
        if worker.department in self._departments:
            self._departments[worker.department].append(worker)
        else:
            tmp = []
            tmp.append(worker)
            self._departments[worker.department] = tmp

