a_num = None

while a_num is None:
    a_num = input("Number? ")
    
    if not a_num.isnumeric():
        print("{0} isn't a number!".format(a_num))
        a_num = None
        
a_num = int(a_num)

print(10 + a_num)