
# "as if":
#  numbers = [1, 2, 3, 4, 6]
#   -or-
#  numbers = range(0,10)

# def add_together(numbers):    
#     sum = 0
#     for n in numbers:
#         sum += n
#         
#     return sum
# 
# #total = add_together(range(0,10))
# total = add_together([1, 2, 4, 6])
# print("Total: " + str(total))
# 
# 
# # Functions don't have to return values:
# 
# def greet_humans(humans):
#     for name in humans:
#         print("Hello, " + name + "!")
#         
#     return
#     
# humans = ["Jim", "Joe", "Jill", "Jake"]
# 
# greet_humans(humans)

# def gimme_four():
#     return 4
#     
# def concat_three(first, second, third):
#     return first + second + third
#     
# print("The num is: " + str(gimme_four()))
# print(concat_three("Joe", "James", "John"))
# print("Concat: " + concat_three(3, 7, 10))
# 


def format_color(hue, saturation, value):
    print("H: " + str(hue))
    print("S: " + str(saturation))
    print("V: " + str(value))
    
format_color(180, .4, .3)

format_color(hue=160, saturation=.3, value=.2)

format_color(saturation=.3, value=.2, hue=160)
format_color(.3, .2, 160) # RONG!

format_color(180, value=.2, saturation=.3)
