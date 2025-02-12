import sys
from Engine import Engine
from Util import Util
from Defs import commands,worker_type,args
from typing import List

class OrganizationApp:

    def __init__(self):
        self.engeine = Engine()

    def Run(self):
        arg = 'welcome'
        arg = arg.split()
        self.Read_Command(arg)

        print('+++++++Testing:\n\n\n\n')

        print('add_add_employee:')

        a = ['add_employee ITZIK_manc nagarot_manc 10 CEO 1',
            'add_employee ITZIK_manc nagarot 10 CEO',
            'add_employee ITZIK_manc2 nagarot 10 CEO',
            'add_employee ITZIK_FAIL nagarot 10 CTO 5',
            'add_employee ITZIK2 nagarot_manc 10 CTO',
            'add_employee ITZIK2 dev 10 CTO 1',
            'add_employee ITZIK3 client 10 CTO 1',
            'add_employee ITZIK4 dev 10 CTO 2',
            'add_employee ITZIK5 client 10 CTO 3',
            'add_employee ITZIK6 client 10 CTO 3',
            'add_employee ITZIK7 dev 10 CTO 2',]

        for x in a:
            #arg = input("Please enter a command: ")
            print(x)
            arg = x
            arg = arg.split()
            self.Read_Command(arg)

        print('tree:\n')
        self.engeine.print_tree()

        print("\n///////////////////////////////////////////\n")
        print('print_dep:\n')
        arg = 'print_dep'
        arg = arg.split()
        self.Read_Command(arg)

        print("\n///////////////////////////////////////////\n")

        print("assign_manager:\n")

        d = ['assign_manager 101 102',
             'assign_manager 2 101',
             'assign_manager 101 2',
             'assign_manager 6 2',
             'assign_manager 5 1',]
        for x in d:
            # arg = input("Please enter a command: ")
            print(x)
            arg = x
            arg = arg.split()
            self.Read_Command(arg)

        print('tree:\n')
        self.engeine.print_tree()
        print('tree:\n')
        self.engeine.print_dep()

        print("\n///////////////////////////////////////////\n")

        print('delete_employee:\n')

        d =['delete_employee 101',
            'delete_employee 3',
            'delete_employee 7',
            'delete_employee 5',]
        for x in d:
            #arg = input("Please enter a command: ")
            print(x)
            arg = x
            arg = arg.split()
            self.Read_Command(arg)

        print('tree:\n')
        self.engeine.print_tree()
        self.engeine.print_dep()

        print("\n///////////////////////////////////////////\n")

        print('print_employee:\n')
        d =['print_employee 101',
            'print_employee 1',
            'print_employee 2',
            'print_employee 6',]
        for x in d:
            #arg = input("Please enter a command: ")
            print(x)
            arg = x
            arg = arg.split()
            self.Read_Command(arg)


        print("End Testing ")
        """
        print("Welcome to Compeny Worker Menegment")
        while True:
            arg = input("Please enter a command: ")
            arg = arg.split()
            self.parser(arg)
        """


#Reading
    def Read_Command(self,args: List) -> None:

        if not self.validate_command_exist(args[0]):
            return
        elif args[0] == commands.welcome.name:
            return Util.print_authors()

        elif args[0] == commands.print_org.name:
            self.engeine.print_tree()

        elif args[0] == commands.print_dep.name:
            self.engeine.print_dep()

        elif args[0] == commands.add_employee.name:
            return self.add_employee_parser(argoments = args)

        elif args[0] == commands.delete_employee.name:
            return self.delete_employee_parser(argoments = args)

        elif args[0] == commands.print_employee.name:
            return self.print_employee_parser(argoments = args)

        elif args[0] == commands.assign_manager.name:
            return self.assign_manager_parser(argoments = args)
        elif args[0] == commands.quit.name:
            sys.exit(0)
        else:
            return


##Parsing:

    def add_employee_parser(self,argoments: List) -> None:
        worker_data = {}

        if len(argoments) < 5:
            Util.Logger(msg ="not enough argoment for command add_add_employee", type ='e')
            return

        if argoments[3].isdigit():
            worker_data[args.age.name] = int(argoments[3])
        else:
            Util.Logger(msg ='age must be a number' ,type ='e')
            return False

        if len(argoments) == 6:
            if argoments[5].isdigit():
                worker_data[args.manager_id.name] = int(argoments[5])
            else:
                Util.Logger(msg ='manager id must be a number',type ='e')
                return False

        worker_data[args.command.name]    = argoments[0]
        worker_data[args.name.name]       = argoments[1]
        worker_data[args.department.name] = argoments[2]
        worker_data[args.type.name]       = argoments[4]


        if self.validate_add_employee_data(worker_data = worker_data):
            self.engeine.add_employee(worker_data = worker_data)

        return
    def delete_employee_parser(self,argoments: List) -> None:
        if not argoments[1].isdigit():
            Util.Logger(msg='employee id must be a number', type='e')
            return
        if self.validate_delete_employee_data(id = int(argoments[1])):
            self.engeine.delete_worker(id = int(argoments[1]))
    def assign_manager_parser(self, argoments: List) -> None:
        if not argoments[1].isdigit():
            Util.Logger(msg='employee id must be a number', type='e')
            return

        if not argoments[2].isdigit():
            Util.Logger(msg='manager id must be a number', type='e')
            return
        if self.validate_assign_manager_data(worker_id = int(argoments[1]), manager_id = int(argoments[2])):
            self.engeine.asign_manager(worker_id = int(argoments[1]), manager_id = int(argoments[2]))
    def print_employee_parser(self, argoments: List) -> None:
        if not argoments[1].isdigit():
            Util.Logger(msg='employee id must be a number', type='e')
            return
        if self.validate_print_employee_data(id = int(argoments[1])):
            self.engeine.print_worker(id = int(argoments[1]))



 ##Data Validation

    def validate_delete_employee_data(self,id:int) -> bool:
        worker = self.engeine.find_worker(id = id)
        if not worker:
            Util.Logger(msg ='Worker Not Found cannot remove this worker', type = 'e')
            return False

        if worker.employees:
            Util.Logger(msg='this worker is manager cannot remove this worker', type='e')
            return False

        return True
    def validate_print_employee_data(self,id: int) -> bool:
        worker = self.engeine.find_worker(id = id)
        if not worker:
            Util.Logger(msg ='Worker Not Found cannot print this worker', type = 'e')
            return False

        return True
    def validate_assign_manager_data(self, worker_id: int, manager_id: int) -> bool:
        worker = self.engeine.find_worker(id = worker_id)
        if not worker:
            Util.Logger(msg='Worker Not Found cannot remove this worker', type='e')
            return False

        manager = self.engeine.find_worker(id = manager_id)
        if not manager:
            Util.Logger(msg='manager Not Found cannot remove this worker', type='e')
            return False

        if worker.manager_id == manager_id:
            Util.Logger(msg="this worker alredy belong to the manger", type='e')
            return False

        return True

        if worker.employees:
            Util.Logger(msg='this worker is manager cannot remove this worker', type='e')
            return False

        return True

        return True
    def validate_add_employee_data(self, worker_data: dict) -> bool:

        if worker_data[args.type.name] not in worker_type.__members__:
            Util.Logger(msg ='Worker type must be from worker type list', type = 'e')
            return False

        if worker_data[args.type.name]  == worker_type.CEO.name and args.manager_id.name in worker_data:
            Util.Logger(msg ='CEO can not get manager_id', type = 'e')
            return False

        if worker_data[args.type.name] != worker_type.CEO.name and args.manager_id.name not in worker_data:
            Util.Logger(msg = "The only worker that can be without maneger is CEO" , type = 'e')
            return False

        if args.manager_id.name in worker_data:
            manager = self.engeine.find_worker(id = worker_data[args.manager_id.name])
            if not manager:
                return False

            if manager.department != worker_data[args.department.name] and worker_data[args.manager_id.name] != 1:
                Util.Logger(msg ='You can not set this worker to this manager with other department', type = 'e')
                return False

        return True
    def validate_command_exist(self, comand:str) -> bool:
            if comand not in commands.__members__:
                Util.Logger(msg = f"{self.comand} is not in the command list",type ='e')
                return False
            return True
