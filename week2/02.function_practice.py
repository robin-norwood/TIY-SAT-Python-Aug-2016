#
# Write a function call "bite_me" that takes bites off of a string and prints them out
#
# bite_me("Lemon")
#
# prints:
# Lemon
# Lemo
# Lem
# Le
# L

# 1: print the whole string
# 2: print everything before the last character
# 3: print everything before that
#  ... until we print just the first character

def bite_me(word):
    """Given a string, print successively smaller bites of it"""
    for c in range(len(word), 0, -1):
        print(word[0:c])
        
# bite_me("Lemon")
# bite_me("Don't cry for me argentina")
# bite_me("")
# bite_me(37)

# Write a function called "square_list" that takes a list of numbers and returns a list of squares of those numbers:

def square_list(numbers):
    the_squares = []
    for n in numbers:
        the_squares.append(n ** 2)
        
    return the_squares

assert square_list([1, 2, 4]) == [1, 4, 16]
assert square_list([3]) == [9]
assert square_list([]) == []

#print(square_list([1, 2, 4]))

# Write a function that asks the user for numbers until they hit "enter", and prints the squares.

# 1. Make a new (empty) list
# 2. Take input to fill the list with numbers
# 3. Call square_list with that list, and save the return value
# 4. Append it to empty list
# 5. Print appended list.

def input_squares():
    input_numbers = []

    while True:
        the_value = input("Enter a number: ")
        # Need to stop when they don't enter anything
        if not the_value:
            break
        
        the_value = int(the_value)
        input_numbers.append(the_value)

    print(square_list(input_numbers))

input_squares()
