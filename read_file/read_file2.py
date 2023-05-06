filename = 'country_info.txt'

with open(filename, encoding='utf-8') as country_file:
    for row in country_file:
        data = row.strip().split('|')
        print(data)

# print(data[1])

