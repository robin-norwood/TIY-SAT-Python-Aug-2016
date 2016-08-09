# coding: utf-8
pets = {'cat', 'dog', 'goldfish', 'charzard', 'betta', 'turtle', 'pikachu'}
mammals = {'cat', 'dog', 'cow', 'weasel', 'rabbit', 'pikachu'}
pokemons = {'charzard', 'pikachu', 'squirtle', 'ditto'}
pets
mammals
pokemons
pets.intersection(mammals)
pets.intersection(pokemons)
pets.union(pokemons)
pets.difference(pokemons)
if 'turtle' in pets.difference(pokemons): print("A turtle is a real pet, not a pokemon")
pets
pets
pets.pop('betta')
pets.pop()
pets
pets.remove('cat')
pets
list(pets)
list(pets) + "cat"
list(pets) + ["cat"]
list(pets)
pets
some_numbers = [3, 4, 5, 1, 1, 3, 7, 138]
some_numbers
set(some_numbers)
some_numbers = list(set(some_numbers))
some_numbers
selected_pet = None
if not selected_pet: print("No pet selected")
prices = {'dog': 3.95, 'cat': 1.38, 'goldfish': .50, 'turtle': None}
if not prices['turtle']: print("No turtle yet!")
if not prices['dog']: print("No turtle yet!")
if not prices['minnow']: print("No turtle yet!")
type("Hello")
type(hello)
type(5)
type(5.0)
type([1, 2, 3, 4]
)
prices
type(prices)
list((1, 2, 3, 4))
type((1, 2, 3, 4))
my_name = "Joe"
your_name = "Bob"
if type(my_name) == type(your_name): print("Yes, they are the same")
my_name = False
if type(my_name) == type(your_name): print("Yes, they are the same")
id(your_name)
my_name = your_name
id(your_name)
first_list = [1, 2, 3]
second_list = [1, 2, 3]
id(first_list)
id(second_list)
second_list = first_list
id(first_list)
id(second_list)
first_list += [5]
first_list
second_list
id(first_list)
id(first_list[0])
id(second_list[0])
an_int = 3000
another_int = 2995 + 5
id(an_int)
id(another_int)
a_list = ["Robert Downey Jr.", "Tom Cruise", "Matt Damon"]
b_list = a_list
id(a_list)
id(b_list)
b_list = ["Robert Downey Jr.", "Tom Cruise", "Matt Damon"]
id(b_list)
a_list == b_list
a_list is b_list
a_list.pop()
a_list
b_list
True == True
False == False
id(True)
id( 12 == 12)
id(None)
None is None
None == None
"Joe" == "Joe"
"Joe" is "Joe"
Joe[1] = 'i'
name = "Joe"
name[1] = 'i'
first = [1, 2, 3]
second = [1, 2, 3]
first == second
first is second
third = first
third is first
third[0] = "monkey"
third
first
second
cats = ["Blackie", "Cranky", "Mu-Mu", None]
if cats[3] is None: print("Hey, we have room for another cat!")
cats[3] = "Stinky"
cats
if cats[3] is None: print("Hey, we have room for another cat!")
if cats[3] is not None: print("NO MORE CATS")
cats[1] = None
cats
get_ipython().magic('save 01.interactive.more_variables 1-110')
