from dataclasses import dataclass


@dataclass()
class Person:

    name = str
    role = str
    age = int

    def __init__(self, name, role, age):
        self.name = name
        self.role = role
        self.age = age


etornam = Person('Etornam', 'Shipment', 25)
amexo = Person('Etornam', 'Shipment', 25)
ben = Person("Benjamin", 'Clerk', 34)


print(ben)
print(id(etornam))
print(etornam == amexo)