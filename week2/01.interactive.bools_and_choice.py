# coding: utf-8
a = True
b = False
a
b
c = true
print(a)
not a
not b
not not a
not not not a
a = not a
a
a = True
b = True
c = False
a and b
a and c
b and c
c and a
b or c
a or b
a or b or c
(a or b) or c
a
b
c
a and not c
a
c
if a: print ("'a' is True!")
if b: print("'b' is True!")
if c: print("'cb' is True!")
if c: print("'c' is True!")
if a: print ("'a' is True!")
if b: print("'b' is True!")
if c: print("'c' is True!")
if a or c: print("Either a or c is True")
if c or a: print("Either a or c is True")
if c and a: print("Either a or c is True")
if a and b or not c: print("Huh???")
if (a and b) or (not c): print("Huh???")
str(5)
bool("Hello")
bool("")
bool(" ")
bool("afsdaf")
name = "Joe"
if name: print("Hello, " + name)
name = ""
if name: print("Hello, " + name)
bool(5)
bool(0)
bool(-1)
bool(0.0)
bool(0.000000000001)
bool("False")
bool([])
people = ["Joe", "Jan", "Jill", "Jaxamaxmillion"]
if(people): print("OH NO! PEOPLE!")
people.pop()
people.pop()
people.pop()
people.pop()
if(people): print("OH NO! PEOPLE!")
people
bool([1, 2, 3])
bool([False])
bool({})
bool({'value': False})
if name: print("Hello, " + name)
name
if bool(name): print("Hello, " + name)
5 == 5
3 > 8
8 > 3
3 < 8
3 <= 8
3 <= 3
3 >= 3
"lost" > "found"
"lost" < "found"
3.14 > 3
2 >= 2.0
2 == 2.0
"one" == "two"
5 == "five"
[1, 2, 3] == [1, 2, 3]
[1, 2, 3] == [1, 2] + [3]
[1, 2, 3] == [1, 2] + ["3"]
3 == "3"
2 != 4
2 != 2
2 != 2.0
"eggs" in "ham and eggs"
5 in [1,2, 3, 4, 6]
5 in [1,2, 3, 4, 5, 6]
"5" in [1,2, 3, 4, 5, 6]
"5" in [1,2, 3, 4, "5", 6]
5 not in [1, 2, 3, 4, 5]
5 not in [1, 2, 3, 4]
animals = {"Panda": "Steve", "Frog": "Froggy", "wildebeast": "Lemmy"}
animals
"frog" in animals
"Frog" in animals
"Cat" in animals
choice = "Panda"
if choice in animals: print("Yes! We have a " + choice)
if choice in animals: print("Yes! We have a " + choice ". His name is " + animals[choice])
if choice in animals: print("Yes! We have a " + choice + ". His name is " + animals[choice])
animals
choice
choice = "wildebeast"
if choice in animals: print("Yes! We have a " + choice + ". His name is " + animals[choice])
choice = "dog"
if choice in animals: print("Yes! We have a " + choice + ". His name is " + animals[choice])
animals[choice]
if choice in animals: print("Yes! We have a " + choice ". His name is " + animals[choice])
if choice in animals: print("Yes! We have a " + choice + ". His name is " + animals[choice])
get_ipython().magic('save 01.interactive.bools_and_choice 1-119')
