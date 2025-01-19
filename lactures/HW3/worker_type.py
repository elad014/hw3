import enum
from enum import Enum

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

    @classmethod
    def print_worker_type_list(cls):
        for t in cls:
            print(f'{t.value} : {t.name}')

if __name__ == '__main__':

    worker_type.print_worker_type_list()