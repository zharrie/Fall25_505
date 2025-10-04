import csv
with open("ch6_labs.csv") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row[-1])
        
