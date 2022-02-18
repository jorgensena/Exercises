
class AllStaff:
    def __init__(self, name, age, emp_id, birth_date, job_title):
        self.name = name
        self.age = age
        self.emp_id = emp_id
        self.birth_date = birth_date
        self.job_title = job_title

    def show(self):
        print(f"{self.name} is {self.age} years old born on {self.birth_date},"
              f"\nwith the id {self.emp_id}. {self.name} has the job "
              f"{self.job_title}")


class Management(AllStaff):
    def __init__(self, name, age, emp_id, birth_date, job_title, car):
        super().__init__(name, age, emp_id, birth_date, job_title)
        self.car = car

    def show(self):
        print(f"{self.name} is {self.age} years old born on {self.birth_date},"
              f"\nwith the id {self.emp_id}. {self.name} has the job "
              f"{self.job_title} and can drive a {self.car}")


class Clerical(AllStaff):
    def __init__(self, name, age, emp_id, birth_date, job_title, typing_speed):
        super().__init__(name, age, emp_id, birth_date, job_title)
        self.typing_speed = typing_speed

    def show(self):
        print(f"{self.name} is {self.age} years old born on {self.birth_date},"
              f"\nwith the id {self.emp_id}. {self.name} has the job "
              f"{self.job_title} and can type at {self.typing_speed} words/min")

class Factory(AllStaff):
    pass


# MAIN ROUTINE


