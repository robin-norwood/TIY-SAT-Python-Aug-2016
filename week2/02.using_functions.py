# coding: utf-8
numbers = list(range(10,20))
numers
numbers
print(numbers)
print("a string")
print("I have " + str(len(numbers)) + " numbers in my list")
get_ipython().magic('pinfo numbers')
numbers.pop()
numbers.sort()
numbers
numbers.reverse()
numbers
numbers.sort()
numbers
get_ipython().magic('pinfo sorted')
sorted(numbers)
numbers.reverse()
numbers
new_numbers = sorted(numbers)
new_numbers
numbers
new_numbers
for num in new_numbers.reverse():
    print("Number: " + str(num))
    
ret_value = new_numbers.reverse()
ret_value
type(ret_value)
new_numbers.reverse()
for num in new_numbers:
    print("Number: " + str(num))
    
get_ipython().magic('pinfo new_numbers.reverse')
copy_of_new_numbers = new_numbers.copy()
copy_of_new_numbers
