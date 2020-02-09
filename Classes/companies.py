class Company:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact


class Drug_Insp(Company):

    def __init__(self, name, contact, specialty, colleague):
        super().__init__(name, contact)
        self.specialty = specialty
        self.colleague = colleague


Inspector_1 = Drug_Insp("Curtis", "0244987678", "supervisor", "Mr Salih")

print(Inspector_1.colleague)