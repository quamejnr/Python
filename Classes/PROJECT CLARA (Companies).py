from Classes.companies import Company

Ernest_chemist = Company('Ernest Chemist', '0244483798', 'P.O.Box 42', 'Kaneshie', True)
Danadams = Company ('Danadams Company Limited', '0244988176', 'P.O.Box 44', 'Spintex', False)

ernest_info = Ernest_chemist.name, Ernest_chemist.contact, Ernest_chemist.postal_address, Ernest_chemist.location, Ernest_chemist.importer
danadams_info = Danadams.name, Danadams.contact, Danadams.postal_address, Danadams.location, Danadams.importer

name = input("Enter company's name: ")

if name == "Ernest Chemist":
    print(Ernest_chemist.address())

while True:

    intro = input ('Hello my name is Bliss and I\'m here to help you!'
                   '\nType importer status to know the importer status of a company'
                   '\nType info for general information on the company: ')

    if intro.casefold() == "importer status":
        companys_name = (input('Name of Company? ')).casefold()

        if companys_name == "ernest chemist":
            print(Ernest_chemist.importer_status())

        elif companys_name == "danadams":
            print(Danadams.importer_status())

        else:
            print("company not found")

    elif intro.casefold() == "info":
        companys_name = (input('What Company are you searching for: ')).casefold()

        if companys_name == "ernest chemist":
            print(str(ernest_info) + "\n")

        elif companys_name == "danadams":
            print (danadams_info)

        else:
            print("company not found")