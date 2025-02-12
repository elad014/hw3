from employee import employee


class worker(employee):

    def __init__(self,name: str, department: str, age: int ,type: str,manager_id: int):

        super().__init__(name = name, department = department, age = age)
        self.type = type
        self.manager_id = manager_id
        self.director = False


    def is_director(self):
        return self.director
    def _verify_is_a_director(self):
        if self.manager_id == 1:
            self.director = True
    def get_detail(self):
        return (f'{super().get_detail()}\n'
                f'manager_id = {self.manager_id}')


