import sys

from defs import *
from view import *


def main():
    choice = ViewModels().start_menu()

    if choice == 'Перейти до покупки':
        choice = ViewModels().choose_goods()

        if choice == "Кава":
            coffe = choose_coffe(choice)
            choice_of_milk(coffe)
            quantity_of_the_desired_product(choice, choise)

        elif choice == "Смаколики":
            choice, choise = yummy(choice)
            quantity_of_the_desired_product(choice, choise)

        elif choice == 'Відміна':
            cleaning_basket()

        elif choice == 'Переглянути кошик':
            receipt(clients_code)

        elif choice == 'Оплата':
            clients_code = discount()
            receipt(clients_code)

    elif choice == "Персонал":
        return loginPersonal()

    else:
        sys.exit()


if __name__ == '__main__':
    main()
