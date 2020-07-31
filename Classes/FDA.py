# from practice import rand_msgs


class Clients:

    def __init__(self, name, location, postal_address, importer_status):
        self.name = name
        self.location = location
        self.postal_address = postal_address
        self.importer_status = importer_status

    def importer(self):
        return "Importer validity of {0.name} located at {0.location} is {0.importer_status}".format(self)

    def postal_add(self):
        return "Postal address of {0.name} is {0.postal_address}".format(self)

    def location_add(self):
        return "{0.name} is located at {0.location}".format(self)

    def __repr__(self):
        return f'Clients({self.name}, {self.location}, {self.postal_address}, {self.importer_status})'

    def __str__(self):
        return "{0.name} is located at {0.location}. " \
               "\nThe postal address is {0.postal_address} and its importer status is {0.importer_status}".format(self)


clients = [
    Clients("Ernest Chemist", "Alajo", "P.O.Box 42", True),
    Clients("Danadams Limited", "Kaneshie", "P.O.Box 38", False),
    Clients("Oson's Chemist Limited", "Okponglo", "P.O. Box 18473", True),
    Clients("Daniel Okine Chemist", "Osu", "P.O.Box 543", True),
    Clients("Ernest Chemist", "Spintex", "P.O.Box 44", False)
]

print("Hello! My name is Bliss. Another day, another yay!")

# TODO: Include random.choice function to pick a random string from a list of choices to make
#  bots more relational and unpredictable


while True:
    print(
          "\nHow may I be of assistance?"
          "\na: Find a company's location address"
          "\nb: Find a company's postal address"
          "\nc: Find a company's importer status"
          "\nd: Find the general info of a company")

    query1 = input()

    if query1.casefold() == "a":

        query2 = input("what company's location address do you want to know?\n")
        for client in clients:
            if query2.casefold() in client.name.casefold():
                print(client.location_add())
                print()

    elif query1.casefold() == "b":

        query2 = input("what company's postal address do you want to know?\n")
        for client in clients:
            if query2.casefold() in client.name.casefold():
                print(client.postal_add())
                print()

    elif query1.casefold() == "c":

        query2 = input("what company's importer status do you want to know?\n")
        for client in clients:
            if query2.casefold() in client.name.casefold():
                client.importer()
                print()

    elif query1.casefold() == "d":

        query2 = input("what company's general info do you want to know?\n")
        for client in clients:
            if query2.casefold() in client.name.casefold():
                print(client)
                print()

    elif query1.casefold() not in "abcd":
        print("Option not available")
        print()

    print("Can I be of further assistance \nYes/No")

    query3 = input()

    if query3.casefold() in "yes":
        continue
    else:
        print("Have a beautiful day!")
        break

