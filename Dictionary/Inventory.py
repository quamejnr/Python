# code to count an inventory or number of characters in a message


def character_count(message):  # input a variable containing strings when calling function
    count = {}

    for character in message:
        count.setdefault(character, 0)  # set key and make default value = 0
        count[character] = count[character] + 1  # add one to the value of the key

    return len(count)


stuff = {"rope": 1, 'torch': 6, 'gold coin': 42, "dagger": 1, 'arrow': 12}


def display_inventory(inventory):  # function for displaying the keys and values in a dictionary
    print('Inventory:')
    result = 0
    for k, v in inventory.items():
        result = result + v
        print(f'{v} {k}')  # prints the key and its value in the inventory

    print(f'Total number of items:{result}')  # prints the sum of the values in the inventory

