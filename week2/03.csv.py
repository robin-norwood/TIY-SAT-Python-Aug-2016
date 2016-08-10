import csv

avengers_header = []
avengers = []

with open('avengers.csv', 'rU', encoding='latin-1') as avengers_csv:
    #print(avengers_csv.read())
    csv_reader = csv.reader(avengers_csv)
    avengers_header = next(csv_reader)
    
    for row in csv_reader:
        avengers.append(row)
#        print(row)
        

print("Found {0} avengers in data.".format(len(avengers)))
# print("Header: ")
# print(avengers_header)
# print("---")
# print("First row: ")
# print(avengers[0])
# print("Last row: ")
# print(avengers[-1])

male_count = 0
female_count = 0
other_count = 0

for av in avengers:
#    print("Name: {0}, Gender: {1}".format(av[1], av[4]))
    if av[4] == 'MALE':
        male_count += 1
    elif av[4] == 'FEMALE':
        female_count += 1
    else:
        other_count += 1
        
print("There are {0} males, {1} females, and {2} other".format(male_count,
                                                               female_count,
                                                               other_count))


# find who has the most appearences
# loop over avengers
#    keep track of greatest number of appearences, and which avenger it is
# When done with loop, print out who it is.

most_appearences = 0
who_has_most_appearences = None

for av in avengers:
    if int(av[2]) > most_appearences:
        most_appearences = int(av[2])
        who_has_most_appearences = av[1]

print("{name} is the most experienced avenger, with {app} appearences".format(
    name=who_has_most_appearences,
    app=most_appearences))

