# Using Hash Tables

# Initializing hash table
book = dict()

# Adding items to hash table
book['apple'] = 2.49
book['milk'] = 1.99
book['egg'] = 4.00

# print(True) if 'apple' in book else print(False)
# print(book.get('hush'))


booth = dict()

booth['Kwame'] = True
booth['Helena'] = True


def check_voter(name):
    if booth.get(name):
        print("Kick them out")
    else:
        print("Let them vote")
        booth[name] = True



