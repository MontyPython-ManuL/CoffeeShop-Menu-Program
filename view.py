from easygui import *

coffe_menu = ('images\\c5d3533af5a86bd4966d9206c4ddaaee.gif', 'images\\da318526245381.563536837107b.gif',
             'images\\b8a2d007e93b475b92aea523f75feb92.gif')
yummy_menu = ('images\\1115353179b2a4213ea888579cf50635.gif', 'images\\original.gif', 'images\\croisant.gif')


class ViewModels:
    def start_menu(self):
        choice = buttonbox("Ласкаво просимо в кав'ярню", 'CoffeeShop', ['Перейти до покупки', "Персонал", 'Вихід'],
                           image='images\\212409.gif')
        return choice

    def coffe_menu(self, coffe_menu_list, lst):
        choise = buttonbox(lst, "CoffeeShop", coffe_menu_list, coffe_menu)
        return choise

    def yummy_menu(self, coffe_menu_list, lst):
        choise = buttonbox(lst, "CoffeeShop", coffe_menu_list, yummy_menu)
        return choise

    def choose_goods(self):
        choice = buttonbox("Що бажаєте купити?: ", "CoffeeShop",
                           ['Кава', "Смаколики", 'Оплата', 'Переглянути кошик', "Відміна"],
                           image='images\\763a73bb9b8e0bdf01e02f523946a313.gif')
        return choice

    def do_you_want_to_milk(self):
        milk_yes_no = buttonbox("Бажаєте молоко до кави?", 'Milk', ['Так', 'Ні'], image='images\\35.gif')
        return milk_yes_no

    def choose_milk_type(self, choice_coffe):
        milk = buttonbox(f"З якого молока вам приготувати {choice_coffe}", 'Milk',
                         ['Кокосове', 'Бананове', 'Вівсяне', 'Мигдальне', 'Простому'], image='images\\37.gif')
        if milk == 'Кокосове':
            msgbox(f'Ви вибрали {choice_coffe} на Кокосовому молоці', image='images\\34.gif')
        elif milk == 'Бананове':
            msgbox(f'Ви вибрали {choice_coffe} на Банановому молоці', image='images\\33.gif')
        elif milk == 'Вівсяне':
            msgbox(f'Ви вибрали {choice_coffe} на Вівсяному молоці', image='images\\36.gif')
        elif milk == 'Мигдальне':
            msgbox(f'Ви вибрали {choice_coffe} на Мигдальному молоці', image='images\\35.gif')
        elif milk == 'Простому':
            msgbox(f'Ви вибрали {choice_coffe} на Простому молоці', image='images\\35.gif')

        return milk

    def sales_user_card(self):
        choice2 = buttonbox('Чи є у вас карта на знижку?', 'CoffeShop',
                            ['Бажаєте зареєструвати', 'Я маю знижку', 'Продовжити без знижки'],
                            image='images\\signing-icon-anim.gif')
        return choice2

    def enter_name_user(self):
        name = enterbox("Введіть ваше ім`я")
        return name

    def enter_code_sales_user(self):
        clients_code = enterbox('Введіть свій код на знижку')
        return clients_code

    def view_sales_user_code(self, name, key):
        msgbox(f'{name} Ваш код для знижки - {key}')

    def info_about_discount_sale(self, name, discount_math):
        msgbox(f'{name}, знижка {discount_math}%')

    def enter_number_product(self, choise):
        amounts = enterbox(f'Скільки {choise} вам потрібно?')
        return amounts

    def info_summ_product_in_basket(self, info_chek, summ_product):
        info = f'{info_chek} \n Загальна сума покупки = {summ_product} \n Ваша знижка: 0%'
        var = buttonbox(info, 'CoffeeShop', ['Оплата', 'Повернутись до покупок', 'Видалити позиції'],
                  image='images\\money.gif')
        return var

    def info_error_count_product(self, choise):
        buttonbox(f"На жаль {choise}у такій кількості немає, введіть меншу", "CoffeeShop",
                  ["Меню", "Оплата"], image='images\\giphy.gif')

    def choose_position_for_del(self, pay_k):
        var_choice = multchoicebox('Виберіть позиції для видалення', 'Delete position', pay_k.keys())
        return var_choice

    def view_personal_menu(self):
        choice = buttonbox(f"Вхід дозволено \nНаступні дії?", "CoffeeShop",
                           ['Склад', "Головна"],
                           image='images\\smartparcel-empty-box.gif')
        return choice

    def add_product_personal(self):
        name_product = buttonbox("Де саме ви хочете додати продукт?", 'New', ['Кава', 'Смаколики', 'Назад'],
                  images='images\\99ff0608104912d023a5642ee8baf1b0.gif')
        return name_product

    def change_prod_personal(self, do):
        choose_del = multenterbox(f"Введіть назву продукту для того щоб {do}", 'change',
                                  ['Тип продукту(Кава\Смаколики)', 'Продукт', 'Кількість'])
        return choose_del

    def check_add_prod_to_basket(self, amounts, type_product):
        basket = buttonbox(f"Ви додали до кошика {amounts} {type_product}", 'CoffeeShop', ['Далі'],
                            image='images\\Cjey.gif')
        return basket