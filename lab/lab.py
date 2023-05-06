import csv

filename = 'ingredients.csv'

with open(filename, encoding='utf-8', newline='') as csv_file:
    reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)

    for row in reader:
        print(row)