import sys
from engine import Engine
from Util import commands,worker_type,args,Util

class OrganizationApp:

    def __init__(self):
        self.engeine = Engine()

    def run(self):
        arg = 'welcome'
        arg = arg.split()
        self.parser(arg)

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
            self.parser(arg)

        print('tree:\n')
        self.engeine.print_tree()

        print("\n///////////////////////////////////////////\n")
        print('print_dep:\n')
        arg = 'print_dep'
        arg = arg.split()
        self.parser(arg)

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
            self.parser(arg)

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
            self.parser(arg)

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
            self.parser(arg)


        print("End Testing ")
        """
        print("Welcome to Compeny Worker Menegment")
        while True:
            arg = input("Please enter a command: ")
            arg = arg.split()
            self.parser(arg)
        """
    def parser(self,args):

        if not self.validate_command_exist(args[0]):
            return False

        elif args[0] == commands.welcome.name:
            return Util.print_authors()

        elif args[0] == commands.print_org.name:
            self.engeine.print_tree()

        elif args[0] == commands.print_dep.name:
            self.engeine.print_dep()

        elif args[0] == commands.add_employee.name:
            return self.add_employee_parser(args)

        elif args[0] == commands.delete_employee.name:
            return self.delete_employee_parser(args)

        elif args[0] == commands.print_employee.name:
            return self.print_employee_parser(args)

        elif args[0] == commands.assign_manager.name:
            return self.assign_manager_parser(args)

        elif args[0] == commands.quit.name:
            sys.exit(0)
        else:
            tmp = {args.command.name: args[0]}

    def add_employee_parser(self,argoments):
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


        if self.validate_add_employee_data(worker_data):
            self.engeine.add_employee(worker_data)

        return

    def delete_employee_parser(self,args):
        if not args[1].isdigit():
            Util.Logger(msg='employee id must be a number', type='e')
            return
        if self.validate_delete_employee_data(int(args[1])):
            self.engeine.delete_worker(int(args[1]))

    def validate_delete_employee_data(self,id):
        worker = self.engeine.find_worker(id)
        if not worker:
            Util.Logger(msg ='Worker Not Found cannot remove this worker', type = 'e')
            return False

        if worker.employees:
            Util.Logger(msg='this worker is manager cannot remove this worker', type='e')
            return False

        return True
    def print_employee_parser(self,args):
        if not args[1].isdigit():
            Util.Logger(msg='employee id must be a number', type='e')
            return
        if self.validate_print_employee_data(int(args[1])):
            self.engeine.print_worker(int(args[1]))

    def validate_print_employee_data(self,id):
        worker = self.engeine.find_worker(id)
        if not worker:
            Util.Logger(msg ='Worker Not Found cannot print this worker', type = 'e')
            return False

        return True

    def assign_manager_parser(self, args):
        if not args[1].isdigit():
            Util.Logger(msg='employee id must be a number', type='e')
            return

        if not args[2].isdigit():
            Util.Logger(msg='manager id must be a number', type='e')
            return
        if self.validate_assign_manager_data(worker_id = int(args[1]), manager_id = int(args[2])):
            self.engeine.asign_manager(worker_id = int(args[1]), manager_id = int(args[2]))

    def validate_assign_manager_data(self, worker_id, manager_id):
        worker = self.engeine.find_worker(worker_id)
        if not worker:
            Util.Logger(msg='Worker Not Found cannot remove this worker', type='e')
            return False

        manager = self.engeine.find_worker(manager_id)
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

    def validate_add_employee_data(self, worker_data):

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
            manager = self.engeine.find_worker(worker_data[args.manager_id.name])
            if not manager:
                return False

            if manager.department != worker_data[args.department.name] and worker_data[args.manager_id.name] != 1:
                Util.Logger(msg ='You can not set this worker to this manager with other department', type = 'e')
                return False

        return True

    def validate_command_exist(self, comand):
            if comand not in commands.__members__:
                Util.Logger(msg = f"{self.comand} is not in the command list",type ='e')
                return False
            return True
