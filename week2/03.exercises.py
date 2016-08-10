# 1. Write a function called "plus" that adds two arguments together and returns the result

def plus(x, y):
    return x + y
    
print(plus(2, 3))


assert plus(2, 3) == 5
assert plus(1, 1) == 2
assert plus(-8, 3) == -5
assert plus("John", "Smith") == "JohnSmith"

















# 2. Write a function called "power" that multiplies the first argument by itself a number of times, defined by the second argument. It does not have to handle a second argument < 1

def power(num, mult): # Without using '**'
    res = 1
    for x in range(0,mult):
        # Multiple the "last" value by num
        res = res * num
        
    return res
    
assert power(2, 2) == 4   # 2 * 2
assert power(3, 3) == 27  # 3 * 3 * 3
assert power(-4, 2) == 16 # -4 * -4
print(power(5,4))



# Write a function called "join_words" that takes a list of words, and returns a string that is made up of those words joined by " "

print(join_words(["Hello", "my", "name", "is", "Nibor"]))
# "Hello my name is Nibor"














# 3. Write a function called "greatest" that takes a list returns the largest (>) value in that list.

assert greatest([1, 2, 3, 4]) == 4
assert greatest([-4, 8, 3, 1]) == 8
assert greatest(["Alice", "Joe", "James"]) == "Joe"



# 4. Write a function called fizz_buzz that takes a single argument, and integer. Iterate from 1 to the given integer, and for each number:
#   - If the number is evenly divisible by 3, print Fizz
#   - If the number is evenly divisible by 5, print Buzz
#   - So, if the number is evenly divisible by both 3 and 5, print FizzBuzz
#   - Otherwise, print the number itself
#
# Output will look like:
#
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# ...