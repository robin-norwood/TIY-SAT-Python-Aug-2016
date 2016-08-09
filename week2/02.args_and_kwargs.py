def concat_three(first, second, third):
    return first + second + third

# Error:     
#print(concat_three("one", "two"))

def concat_all(*args):
    print("TYPE: " + str(type(args)))
    return ' '.join(args)
    
print(concat_all("Jimminy", "Cricket", "Steve"))

def concat_with(sep, *strings):
    return sep.join(strings)
    
print(concat_with(", ", "milk", "eggs", "flour", "sugar"))

print(concat_with(", "))

def print_options(**options):
    for (k, v) in options.items():
        print('<option value="' + k + '">' + v + '</option>')
        
print_options(TX="Texas", NJ="New Jersey", CA="California")



## Default arguments

def repeat(num=3):
    for x in range(0,num):
        print("Repeat!")
    
#repeat()
repeat(5)

def crazy_args(first, second, *args, **kwargs):
    """Show off how crazy you can get with args."""
    
    print("First: " + str(first))
    print("second: " + str(second))
    for arg in args:
        print("ARG: " + str(arg))
    for (k, v) in kwargs.items():
        print("KEY: " + str(k) + ", VALUE: " + str(v))
        
crazy_args(5, "second", 2, 3, 5, foo="bar", baz=12.5)

print(crazy_args.__doc__)
