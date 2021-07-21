
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Name deleted!")
        self.first = None
        self.last = None

    @property
    def email(self):
        return f'{self.first.lower()}.{self.last.lower()}@email.com'

    @classmethod
    def from_string(cls, name):
        first, last = name.split(" ")
        return cls(first, last)

    def __str__(self):
        return f"{self.first} {self.last}"


name_1 = Employee("Akua", "Bliss")
name_2 = Employee("Gail", "Ofosu")


print(name_1.fullname)
print(name_2.first)
name_1.from_string('Kwame Akuamoah-Boateng')
print(name_1)







