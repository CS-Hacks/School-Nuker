################ Imports ################
from os import system
from db import sql_database_remover

################ Printing Options ################
system('clear|cls')
print('-' * 100)
print(
'-' * 10, 'This is a script for nuking your school!!')
print('-' * 100)
print()


#### Printing Options ####
while True:
    print("Press 1 to run SQL Database Nuker")
    print("Press 0 to quit")
    choice = input('What is your choice? ')
# Checking if choice is integer
    if choice.isdigit():
        choice = int(choice)
        if 0 <= choice <= 1:
            break
        else:
            system('clear|cls')
            print('-' * 100)
            print(
            '-' * 10, 'This is a script for nuking your school!!')
            print('-' * 100)
            print()
            continue
    else:
        system('clear|cls')
        print('-' * 100)
        print(
        '-' * 10, 'This is a script for nuking your school!!')
        print('-' * 100)
        print()
        continue


################### Calling Functions ###################
if choice == 0:
    system('clear|cls')
    quit()
elif choice == 1:
    system('clear|cls')
    print('-' * 100)
    print(
    '-' * 10, 'This is a script for nuking your school!!')
    print('-' * 100)
    print()
    sql_database_remover()
