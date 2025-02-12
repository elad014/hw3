from Employee import Employee


class Worker(Employee):

    def __init__(self,name: str, department: str, age: int ,type: str,manager_id: int):

        super().__init__(name = name, department = department, age = age)
        self._type = type
        self._manager_id = manager_id
    @property
    def type(self) -> None:
        return self._type

    @property
    def manager_id(self) -> None:
        return self._manager_id

    @manager_id.setter
    def manager_id(self, id: int) -> None:
        self._manager_id = id

    def get_detail(self):
        return (f'{super().get_detail()}\n'
                f'manager_id = {self._manager_id}')


