import enum

class Util:

    @staticmethod
    def print_authors():
        print("//////////////////////////////////////")
        print("/// id:  308542141                ////")
        print("/// name: Elad Natan              ////")
        print("/// mail: elad.glx@email.com      ////")
        print("//////////////////////////////////////")
        print("/// id:   207930868               ////")
        print("/// name: Ofir Goldstein          ////")
        print("/// mail: goldsteinofir@gmail.com ////")
        print("//////////////////////////////////////")

class k_worker_type(enum.Enum):

    SW_DEVELOPER = 1
    HW_DEVELOPER = 2
    TECH_LEAD = 3
    TEAM_LEADER = 4
    HR_MANAGER = 5
    RECRUITER = 6
    ACCOUNTANT = 7
    FINANCE_MANAGER = 8
    DIRECTOR = 9
    CTO = 10
    CEO  = 11

class saved_commands(enum.Enum):

    welcome = 1
    add_employee = 2
    delete_employee = 3
    print_employee = 4
    assign_manage = 5
    print_org = 6

class defs(enum.Enum):

    command = 1
    name = 2
    department = 3
    type = 4
    age = 5
    manager_id = 6