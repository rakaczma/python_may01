import csv

filename = 'username.csv'

with open(filename, encoding='utf-8', newline='') as csv_file:
    # Sniffer
    sample = csv_file.read()
    file_dialect = csv.Sniffer().sniff(sample)
    # wracamy na początek pliku
    csv_file.seek(0)
    # usunięcie headerów
    csv_file.readline().strip('\n').split(file_dialect.delimiter)

    # reader = csv.reader(csv_file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)

    # przekazujemy doalekt który został znaleziony przez Sniffera
    reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC, dialect=file_dialect)

    for row in reader:
        print(row)

print(f"Delimiter: {file_dialect.delimiter}")
print(f"Escape: {file_dialect.escapechar}")
print(f"Line terminator: {repr(file_dialect.lineterminator)}")