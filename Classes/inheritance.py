# Inheritance: is the process where a class takes the attributes of another class

class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


class SoftwareEngineer(Employee):

    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level

    def work(self):
        print(f"{self.name} is coding")


class Designer(Employee):
    pass


se = SoftwareEngineer('Max', 25, 5_000, 'Senior')
print(se.name, se.age, se.level)
se.work()

