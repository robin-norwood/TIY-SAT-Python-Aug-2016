# Req: Require the user enter something in each field (i.e. - not an empty string). Keep asking until they do.
# Steps:
#  1. Ask the user to enter value for <field> (e.g. name)
#  2. Check whether or not they entered something (len(<the_string>) == 0)
#  3. If they didn't, repeat from #1. If they did, keep going
#
# Ideas:
#   - Maybe use continue
#   - Need a loop! But what kind?
#      - a while loop! - what's the condition?
#      - Condition: Did the user enter some text?


cont = 'yes'
people = []

while cont.lower()[0] != 'n':
    name = ""
    
    while len(name) == 0 or len(name.split(' ')) < 2:
        name = input("Name? ")

    fav_color = input("Favorite color? ")
    age = input("Age? ")

    people.append({'name': name, 'fav_color': fav_color, 'age': age})
    cont = input("Continue? ")

#print(people)

for p in people:
    print("Name: " + p['name'])
    print("Color: " + p['fav_color'])
    print("Age: " + p['age'])
    print("---")
    