import enum


class worker_type(enum.Enum):

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

class commands(enum.Enum):

    welcome = 1
    add_employee = 2
    delete_employee = 3
    print_employee = 4
    assign_manager = 5
    print_org = 6
    print_dep = 7
    quit = 8

class args(enum.Enum): #employee info

    command = 1
    name = 2
    department = 3
    type = 4
    age = 5
    manager_id = 6