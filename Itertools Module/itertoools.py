import itertools


counter = itertools.count(0, 2)

data = [10, 20, 30, 40]

# daily_data = list(zip(counter, data))
# print(daily_data)

# itertools.zip_longest unlike zip will continue to pair until the iterable runs out
daily_data = list(itertools.zip_longest(range(10), data))


# itertools.cycle is used when running a cycle
switch = itertools.cycle(("On", "Off"))
# print("Switch on light")
# print(f'Light is {next(switch)}')
# print("Switch off light")
# print(f'Light is {next(switch)}')

squares = map(pow, range(10), itertools.repeat( 2))

# itertools.starmap allow one to be able to run a function like map with just one arg (iterable)
star_squares = itertools.starmap(pow, [(0, 2), (1, 2), (2, 2)])
pass

# itertools.combinations gives you the different combinations of a list where order is not a factor
letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3, 4, 5]
names = ['Quame', 'Jnr']

comb = itertools.combinations(letters, 2)
for item in comb:
    pass

# itertools.permutations gives you the different permutations of a list where order is a factor
comb = itertools.permutations(letters, 2)
for item in comb:
    pass

# itertools.product gives you the different combinations of a list where item can be repeated many times
comb = itertools.product(numbers, repeat=4)
for item in comb:
    pass

# itertools.chain allows you to combine two or more lists
combined = itertools.chain(letters, numbers, names)
for item in combined:
    pass

dic = {'house A':('Kofi', 'Ama'), 'house B': ('Kwaku', "Abena")}
