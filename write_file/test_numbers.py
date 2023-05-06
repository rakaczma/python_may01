test_numbers = 'numbers.txt'

with open(test_numbers, 'w', encoding='utf-8') as numbers_file:
    for i in range(10):
        numbers_file.write(str(i))