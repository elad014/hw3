from engeine import engeine
from Util import saved_commands,k_worker_type,defs,Util

class OrganizationApp:

    def __init__(self):
        self.E = engeine()

    def run(self):
        arg = 'welcome'
        arg = arg.split()
        self.parser(arg)


        a = ['add_employee ITZIK_manc nagarot 10 CEO 1',
            'add_employee ITZIK_manc nagarot 10 CEO',
            'add_employee ITZIK_manc2 nagarot 10 CEO',
            'add_employee ITZIK_FAIL nagarot 10 CTO 5',
            'add_employee ITZIK2 nagarot 10 CTO 1',
            'add_employee ITZIK3 nagarot 10 CTO 1',
            'add_employee ITZIK4 nagarot 10 CTO 2',
            'add_employee ITZIK5 nagarot 10 CTO 3',
            'add_employee ITZIK6 nagarot 10 CTO 3',
            'add_employee ITZIK7 nagarot 10 CTO 2',]

        for x in a:
            #arg = input("Please enter a command: ")
            arg = x
            arg = arg.split()
            self.parser(arg)
        self.E.print_tree()

        print("///////////////////////////////////////////\n")
        d =['delete_employee 101',
            'delete_employee 3',
            'delete_employee 7',
            'delete_employee 5',]
        for x in d:
            #arg = input("Please enter a command: ")
            arg = x
            arg = arg.split()
            self.parser(arg)
        self.E.print_tree()


        print("///////////////////////////////////////////\n")
        d =['print_employee 101',
            'print_employee 1',
            'print_employee 2',
            'print_employee 6',]
        for x in d:
            #arg = input("Please enter a command: ")
            arg = x
            arg = arg.split()
            self.parser(arg)

        print("Thank you for using FUN in the GROCERY STORE!")


    def parser(self,args):
        if not self.valedate_comand_exist(args[0]):
            return False
        elif args[0] == saved_commands.welcome.name:
            return Util.print_authors()

        elif args[0] == saved_commands.print_org.name:
            self.E.print_tree()

        elif args[0] == saved_commands.print_org.name:
            self.E.print_tree()

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
            if args[5].isdigit():
                worker_data[defs.manager_id.name] = int(args[5])
            else:
                print('[ERROR] manager id must be a number')
                return False

        if self.validate_add_employee_data(worker_data):
            self.E.add_employee(worker_data)
            self.E.num_of_employees += 1

        return

    def delete_employee_parser(self,args):

        if args[1].isdigit():
           self.E.delete_worker(int(args[1]))
           return
        print('[ERROR] id must be a number')
        return False

    def print_employee_parser(self,args):

        if args[1].isdigit():
           self.E.print_worker(int(args[1]))
           return
        print('[ERROR] id must be a number')
        return False

    def asign_manager_parser(self,args):

        if args[1].isdigit():
           self.E.delete_worker(int(args[1]))
           return
        print('[ERROR] id must be a number')
        return False

    def validate_add_employee_data(self, worker_data):

        if worker_data[defs.type.name] not in k_worker_type.__members__:
            print('[ERROR] worker type must be from workerd type list')
            return False

        if worker_data[defs.type.name]  == k_worker_type.CEO.name and defs.manager_id.name in worker_data:
            print('[ERROR] CEO canot get manager_id')
            return False

        if defs.manager_id.name in worker_data:
            manager = self.E.find_worker(worker_data[defs.manager_id.name])
            if not manager:
                print('cant finde manager')
                return False

            if not manager.department != worker_data[defs.department.name]:
                print('you canot set this worker to this manager with other department')
                return False

        return True

    def valedate_comand_exist(self,comand):
            if comand not in saved_commands.__members__:
                print(f"{self.comand} is not in the command list")
                return False
            return True
