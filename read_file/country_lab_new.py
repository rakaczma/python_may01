import csv

filename = 'country_info.txt'

countries = {}

dialect = csv.excel
dialect.delimiter = '|'

with open(filename, encoding='utf-8') as country_file:
    headers = country_file.readline().rstrip('\n').split(dialect.delimiter)

    for index, header in enumerate(headers):
        headers[index] = header.casefold()

    reader = csv.DictReader(country_file, dialect=dialect, fieldnames=headers)

    for row in header:
        countries[row['country'].casefold()] = row
        countries[row['cc'].casefold()] = row

print(countries)

    # for line in country_file:
    #     data = line.strip().split('|')
    #     country, capital, cc, cc3, iac, timezone, currency = data
    #     # teraz chcemy zasilić naszą mapę countries
    #
    #
    #     # tworzymy mapę z danymi
    #     country_info_map = {
    #         'capital': capital,
    #         'timezone': timezone,
    #         'iac': iac,
    #         'currency': currency
    #     }
    #     countries[country.casefold()] = country_info_map
    #     countries[cc.casefold()] = country_info_map

# for key in countries:
#     print(f"KEY: {key}, VALUE: {countries[key]}")

while True:
    selected_country = input("Podaj kraj lub kod: ")

    if selected_country == '0':
        break

    result = countries.get(selected_country.casefold())
    if result:
        print(f"Stolica: {result['capital']}", f"Strefa czasowa: {result['timezone']}",
              f"Kod kierunkowy: {result['iac']}", f"Waluta: {result['currency']}", sep='\n\t')
    else:
        print(f"Nie ma takiego klucza jak {selected_country}")