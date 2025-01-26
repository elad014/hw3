from engine import Engine
from Util import saved_commands,k_worker_type,defs,Util

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


        print("Thank you for using FUN in the GROCERY STORE!")


    def parser(self,args):

        if not self.validate_command_exist(args[0]):
            return False

        elif args[0] == saved_commands.welcome.name:
            return Util.print_authors()

        elif args[0] == saved_commands.print_org.name:
            self.engeine.print_tree()

        elif args[0] == saved_commands.print_dep.name:
            self.engeine.print_dep()

        elif args[0] == saved_commands.add_employee.name:
            return self.add_employee_parser(args)

        elif args[0] == saved_commands.delete_employee.name:
            return self.delete_employee_parser(args)

        elif args[0] == saved_commands.print_employee.name:
            return self.print_employee_parser(args)

        elif args[0] == saved_commands.assign_manager.name:
            return self.assign_manager_parser(args)
        else:
            tmp = {defs.command.name: args[0]}

    def add_employee_parser(self,args):
        if len(args) < 5:
            print("not enough argumants")
            return

        worker_data = {}

        worker_data[defs.command.name]    = args[0]
        worker_data[defs.name.name]       = args[1]
        worker_data[defs.department.name] = args[2]
        worker_data[defs.type.name]       = args[4]

        if args[3].isdigit():
            worker_data[defs.age.name] = int(args[3])
        else:
            print('[ERROR] age id must be a number')
            return False

        if len(args) == 6:
            print(args[5])
            if args[5].isdigit():
                worker_data[defs.manager_id.name] = int(args[5])
            else:
                print('[ERROR] manager id must be a number')
                return False
        if len(args) == 5 and worker_data[defs.type.name] !=  k_worker_type.CEO.name:
            print("Error the only worker that can be without maneger is CEO")
            return False

        if self.validate_add_employee_data(worker_data):
            self.engeine.add_employee(worker_data)
            self.engeine.num_of_employees += 1

        return

    def delete_employee_parser(self,args):

        if args[1].isdigit():
           self.engeine.delete_worker(int(args[1]))
           return
        print('[ERROR] id must be a number')
        return False

    def print_employee_parser(self,args):

        if args[1].isdigit():
           self.engeine.print_worker(int(args[1]))
           return
        print('[ERROR] id must be a number')
        return False

    def assign_manager_parser(self, args):
        print
        if args[1].isdigit():
           self.engeine.asign_manager(int(args[1]), int(args[2]))
           return
        print('[ERROR] id must be a number')
        return False

    def validate_add_employee_data(self, worker_data):

        if worker_data[defs.type.name] not in k_worker_type.__members__:
            print('[ERROR] worker type must be from worker type list')
            return False

        if worker_data[defs.type.name]  == k_worker_type.CEO.name and defs.manager_id.name in worker_data:
            print('[ERROR] CEO can not get manager_id')
            return False

        if defs.manager_id.name in worker_data:
            manager = self.engeine.find_worker(worker_data[defs.manager_id.name])
            if not manager:
                print('cant find manager')
                return False

            if manager.department != worker_data[defs.department.name] and worker_data[defs.manager_id.name] != 1:
                print('You can not set this worker to this manager with other department')
                return False

        return True

    def validate_command_exist(self, comand):
            if comand not in saved_commands.__members__:
                print(f"{self.comand} is not in the command list")
                return False
            return True
