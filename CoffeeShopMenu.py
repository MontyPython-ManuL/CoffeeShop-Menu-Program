import sys

from defs import *
from view import *


def main():
    choice = ViewModels().start_menu()

    if choice == 'Перейти до покупки':
        while True:
            user_choose_product = ViewModels().choose_goods()
            if user_choose_product == "Кава":
                coffe = choose_product(user_choose_product)
                choose_milk = do_you_wanna_milk(user_choose_product)
                if choose_milk:
                    milk_type = choice_of_milk(coffe)
                main_work_with_product_in_data(user_choose_product, coffe)


###

            elif user_choose_product == "Смаколики":
                choice, yummy = user_choose_product(choice)
                main_work_with_product_in_data(choice, yummy)

            elif user_choose_product == 'Відміна':
                cleaning_basket()

            elif user_choose_product == 'Переглянути кошик':
                receipt(clients_code)

            elif user_choose_product == 'Оплата':
                clients_code = main_discount()
                receipt(clients_code)

    elif choice == "Персонал":
        return loginPersonal()

    else:
        sys.exit()


if __name__ == '__main__':
    main()
