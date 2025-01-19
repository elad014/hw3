from engeine import engeine
from dataclasses import dataclass
from worker_type import k_worker_type


# format add_employee <name: str> <department: str> <age: int> <type: str> <manager_id: id>


class OrganizationApp:

    def __init__(self):
        self.E = engeine()

    def run(self):

        c = ['add_employee ITZIK_manc nagarot 10 CEO 1',
            'add_employee ITZIK_manc nagarot 10 CEO',
            'add_employee ITZIK_manc2 nagarot 10 CEO',
            'add_employee ITZIK_FAIL nagarot 10 CTO 5',
            'add_employee ITZIK2 nagarot 10 CTO 1',
            'add_employee ITZIK3 nagarot 10 CTO 1',
            'add_employee ITZIK4 nagarot 10 CTO 2',
            'add_employee ITZIK5 nagarot 10 CTO 3',
            'add_employee ITZIK6 nagarot 10 CTO 3',
            'add_employee ITZIK7 nagarot 10 CTO 2',]

        for x in c:
            #arg = input("Please enter a command: ")
            arg = x
            arg = arg.split()
            tmp = {}

            if len(arg) == 0 or len(arg) > 6:
                print("bad command")
                continue
            tmp['command'] =    arg[0]
            tmp['name'] =       arg[1]
            tmp['department'] = arg[2]
            tmp['age'] =        int(arg[3])
            tmp['type'] =       arg[4]
            if len(arg) == 6 :
                tmp['manager_id'] = int(arg[5])

             #validate command
            if tmp['command'] == 'add_employee':
                #VALIDATE EMPLOYEE
                if tmp['type'] == "CEO" and len(arg) > 5 and tmp['manager_id']:
                    print("ceo canot get manager_id")
                    continue
                if tmp['type'] in k_worker_type.__members__ and tmp['type'] != "CEO" and len(arg) <= 5:
                    print("you must set manager_id to employee")
                    continue
                else:
                    self.E.add_employee(tmp)

        self.print_tree()
        print("Thank you for using FUN in the GROCERY STORE!")



    def parser(self, args):
        # format add_employee <name: str> <department: str> <age: int> <type: str> <manager_id: id>
        args = args.slplit()
        # validate format
        if not args[0].isalpha():
            return print(f"name must be string")
        if not args[1].isalpha():
            print(f"department must be string")
            return False
        elif not args[2].isdigit():
            print(f"age must be int")
            return False
        elif args[3] not in k_worker_type:
            print(f"age {args[3]} is not in the list of allowed workers type")
            return False
        elif args[4] and not args[4].isdigit():
            print(f"manager_id must be int")
            return False
        elif args[3] == k_worker_type.CEO and args[4] and args[4].isdigit():
            print(f"CEO canot get manager_id")
            return False
        elif args[3] == k_worker_type.CEO and self.Organization_tree[0]:
            print(f"Organization can have only a single CEO")
            return False
        # validate type if
        return args

    def search_manager_by_id(self):
        for root in self.E.Organization_tree:
            root.print_manager(3)


    def print_tree(self):
        for root in self.E.Organization_tree:
            root.print_manager(3)