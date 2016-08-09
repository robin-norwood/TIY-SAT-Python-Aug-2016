# <!-- HTML COMMENT -->
# Python comment

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
my_name = "Joe"
name = None

print("Hello, world!")

if my_name:
    # Demonstrating blocks
    print("How do you do, " + str(my_name) + "?")
    print("Are you ready to learn some python?")
    

if "orange" in colors:
    # Nested blocks
    # If orange weren't a color, none of this woiuld run
    name = "Steve" # name initialized above, because we want to show a really long comment on one line. Bad style :(
    print("Orange is a color, " + name)

    # For a really long comment, it's usually better to put in
    # on multiple lines. Much easier to read.
    if "tan" in colors:
        print("So is tan")

    # This next one is True
    if "green" in colors:
        print("So is green")

print("Can you even python, " + name)

