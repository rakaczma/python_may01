menu_options = {
    1: 'Dodanie nowego składnika',
    2: 'Wyświetlenie wszystkich składników',
    3: 'Wyświetlenie składnika po nazwie (like)',
    0: 'Zakończenie programu',
}

# def print_menu():
#     for key in menu_options.keys():
#         print (key, '--', menu_options[key] )
#
# print_menu()

while True:
    print(menu_options)
    action = input("Wybierz opcje: ")
    if action == "1":
        pass
    elif action == "2":
        pass
    elif action == "3":
        pass
    elif action == "0":
        print('Program zostanie zakończony')
        exit()
    else:
        print('Mordo musisz wybrać między 0 a 3!')