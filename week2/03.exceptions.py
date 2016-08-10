a_num = None

while a_num is None:
    a_num = input("Enter a number: ")

    try:
        a_num = int(a_num)
    except ValueError as e:
        print(e)
        print("Uh oh! {0} wasn't a number".format(a_num))
        a_num = None

print(5 + a_num)

