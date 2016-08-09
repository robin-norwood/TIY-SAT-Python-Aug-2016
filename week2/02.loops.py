# while True:
#     name = input("Enter your name: ")
#     print("Hello, " + name)
# 
#     if not name:
#         break
#     
# print("All done!")

# done = False
# 
# while not done:
#     color = input("Gimme a color, fool: ")
#     if not color:
#         done = True
#     else:
#         print(color + " is a real pretty color.")
# 

ponies = ["Pinkie-pie", "Fluffy", "Mr. Butters", "Cranky-stanks"]

# while ponies:
#     pony = ponies.pop()
#     print("Bye bye " + pony)

# for pony in ponies:
#     print("Hello, " + pony)

# people = []
# done = False
# 
# while not done:
#     name = input("Enter your name: ")
#     if name:
#         people.append(name)
#     else:
#         done = True
#         
# print(people)
# 
# # for p in people:
# #     print("Hello " + p)
# 
# while people:
#     print("Hello, " + people.pop() + "!")
# 
# people = []
# 
# while True:
#     name = input("Enter your name: ")
#     if name:
#         people.append(name)
#     else:
#         break
#         
#     print("Adding " + name + " to my list")
#     
# while people:
#     name = people.pop()
#     
#     if len(name) < 2:
#         continue
#         
#     print("Thanks for coming, " + name)
#     

# numbers = [1, 2, 3, 4, 5, 6]
# 
# for num in numbers:
#     if num == 3:
#         continue
#         
#     print(str(num) + " is a great number")

# range works like slice:
# range(start, stop_before, step)
# 
# for num in range(0, 20):
#     if num % 3:
#         continue
#     
#     print("My favorite number is " + str(num))
#         

## For loops and dictionaries

#a_dict = {"first": 1, "second": 2}

colors = {"red": "#ff0000", "green": "#00ff00", "blue": "#3333ff"}

# One way: iterate over keys in dictionary
for c in colors:
    print("Color name: " + c)
    print(" Hex value: " + colors[c])
    print("")

for (c, v) in colors.items():
    print("Name: " + c + ", Value: " + v)
    print("")
    
print("All done")

