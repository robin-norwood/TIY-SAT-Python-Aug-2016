import csv

avengers_header = []
avengers = []

with open('avengers.csv', 'rU', encoding='latin-1') as avengers_csv:
    #print(avengers_csv.read())
    csv_reader = csv.reader(avengers_csv)
    avengers_header = next(csv_reader)
    
    for row in csv_reader:
        avengers.append(row)
        

current_avengers_header = ['URL', 'Name/Alias', 'Gender']

with open('current_avengers.csv', 'w') as current_avengers:
    csv_writer = csv.writer(current_avengers)

    csv_writer.writerow(current_avengers_header)
    for av in avengers:
        if av[3] == 'YES':
            csv_writer.writerow([
                av[0], # URL
                av[1], # Name/Alias
                av[4]  # Gender
            ])
            
