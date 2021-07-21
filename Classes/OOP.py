# OBJECT ORIENTED PROGRAMMING

# Classes are used for more complex data structure other than the primitive data types

# Implementation of Class (a blueprint)

class SoftwareEngineer:

    # class attributes: these attributes belong to the class itself thus the same for every instance
    alias = 'Keyboard Magician'

    def __init__(self, name, age, level, salary):
        # instance attributes: these attributes only belong to the instances and not the class
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    # instance method
    def code(self):
        print(f'{self.name} is writing code...')

    def __str__(self):
        information = f'name: {self. name}, age: {self.age}, level: {self.level}'
        return information

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


# instance
se1 = SoftwareEngineer('John', '25', 'Junior', 5_000)
se2 = SoftwareEngineer('Lisa', 35, 'Senior', 8_000)
se3 = SoftwareEngineer('Lisa', 35, 'Senior', 8_000)
# Accessing instance attributes
# print(se1.salary)

# Accessing class instance
# print(se1.alias)
# print(SoftwareEngineer.alias)

# print(se2 == se3)


