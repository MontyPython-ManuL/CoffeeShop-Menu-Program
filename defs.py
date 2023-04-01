import os.path
import random
import time
import json
from view import *
import sys


class WorkDataJson:
    def __init__(self):
        self.basket = os.path.join('data', 'basket.json')
        self.clients_base = os.path.join('data', 'clients_base.json')
        self.menu = os.path.join('data', 'menu.json')
        self.staff = os.path.join('data', 'staff.json')

    def read_basket_file(self):
        with open(self.basket, "r", encoding='utf-8') as basket:
            return json.load(basket)

    def read_clients_baza_file(self):
        with open(self.clients_base, "r", encoding='utf-8') as client_data:
            return json.load(client_data)

    def read_menu_file(self):
        with open(self.menu, "r", encoding='utf-8') as menu:
            return json.load(menu)

    def read_staff_file(self):
        with open(self.staff, "r", encoding='utf-8') as staff:
            return json.load(staff)

    def write_basket_file(self, input_data):
        with open(self.basket, "w", encoding='utf-8') as basket:
            json.dump(input_data, basket, ensure_ascii=False)

    def write_clients_baza_file(self, input_data):
        with open(self.clients_base, "w", encoding='utf-8') as client_data:
            json.dump(input_data, client_data, ensure_ascii=False)

    def write_menu_file(self, input_data):
        with open(self.menu, "w", encoding='utf-8') as menu:
            json.dump(input_data, menu, ensure_ascii=False)

    def write_staff_file(self, input_data):
        with open(self.staff, "w", encoding='utf-8') as staff:
            json.dump(input_data, staff, ensure_ascii=False)


class CreateDataForUser:
    def __init__(self, discount):
        self.key = 0
        self.discount = discount

    def create_key(self):
        key = self.key = random.randrange(1000000, 9999999)
        return key


class UserDiscount:
    def __init__(self, data_discount):
        self.data_discount = data_discount

    def find_user_discount_in_data(self):
        clients_code = ViewModels().enter_code_sales_user()
        if str(clients_code) not in self.data_discount:
            return 0
        else:
            discount_math = self.data_discount.get(clients_code).get("Сума") / 500
            if discount_math > 20:
                CreateDataForUser(20)
                name = self.data_discount.get(clients_code).get("Імя")
                ViewModels().info_about_discount_sale(name, discount_math)
                return discount_math

    def create_number_of_discount(self):
        key = CreateDataForUser.create_key
        name = ViewModels().enter_name_user()

        ViewModels().view_sales_user_code(name, key)

        self.data_discount[key] = {'Ім`я': name, 'Знижка': 0, 'Сума': 0}
        WorkDataJson().write_clients_baza_file(self.data_discount)

        return key


def main_discount():
    choice = ViewModels().sales_user_card()
    data_discount = WorkDataJson().read_clients_baza_file()

    if choice == 'Бажаєте зареєструвати':
        return UserDiscount(data_discount).create_number_of_discount()

    elif choice == 'Я маю знижку':
        return UserDiscount(data_discount).find_user_discount_in_data()

    elif choice == 'Продовжити без знижки':
        return 0

    else:
        sys.exit()


def choose_product(choice):
    base_menu = WorkDataJson().read_menu_file()
    menu_list = [i for i in base_menu[choice].keys()]
    lst = ""
    for txt in base_menu.get(choice):
        lst += f'{txt} - {base_menu.get(choice).get(txt).get("Ціна")} {base_menu.get(choice).get(txt).get("Валюта")}\n'
    return ViewModels().coffe_menu(menu_list, lst)


def do_you_wanna_milk(choise):
    lst_menu_in_milk = ["Капучино", "Латте", "Флет Уайт", "Раф кава"]
    if choise not in lst_menu_in_milk:
        return choise
    else:
        milk_yes_no = ViewModels().do_you_want_to_milk()
        if milk_yes_no == "Так":
            return True


def choice_of_milk(choice_coffe):
    return ViewModels().choose_milk_type(choice_coffe)


class WorkerProductData:
    def __init__(self, base_menu):
        self.base_menu = base_menu

    def check_product_in_data(self, user_choose_product, type_product, amounts):
        price = self.base_menu.get(user_choose_product).get(type_product).get("Ціна")
        if self.base_menu.get(user_choose_product).get(type_product).get("Кількість") >= int(amounts):
            basket = ViewModels().check_add_prod_to_basket(amounts, type_product)
            data1 = WorkDataJson().read_basket_file()
            if type_product in data1:
                data1[type_product]["Кількість"] = data1[type_product]["Кількість"] + int(amounts)
                data1[type_product]["Ціна"] = data1[type_product]["Кількість"] * price
            else:
                data1[type_product] = {"Кількість": int(amounts), "Ціна": price * int(amounts),
                                 "Валюта": self.base_menu.get(user_choose_product).get(type_product).get("Валюта")}

            WorkDataJson().write_basket_file(data1)
            return basket

        else:
            ViewModels().info_error_count_product(type_product)


def main_work_with_product_in_data(user_choose_product, type_product):
    base_menu = WorkDataJson().read_menu_file()
    amounts = ViewModels().enter_number_product(type_product)
    WorkerProductData(base_menu).check_product_in_data(user_choose_product, type_product, amounts)


def cleaning_basket():
    data = WorkDataJson().read_basket_file()
    data.clear()
    WorkDataJson().write_basket_file(data)


def receipt(clients_code):
    pay_k = WorkDataJson().read_basket_file()
    summ_product = 0.0
    info_chek = ''
    for txt in pay_k:
        info_chek += f'{txt} - {pay_k.get(txt).get("Ціна")} {pay_k.get(txt).get("Валюта")}\n'
        summ_product += pay_k.get(txt).get("Ціна")
    pay_r = WorkDataJson().read_clients_baza_file()
    if clients_code not in pay_r:
        info = ViewModels().info_summ_product_in_basket(info_chek, summ_product)
        msgbox(info, 'CoffeeShop', 'Оплата', image='images\\money.gif')
        discount = 0
    else:
        discount = pay_r.get(clients_code).get("Сума") / 500
        if discount > 20:
            discount = 20
        summ_zn = summ_product - (summ_product * (discount / 100))
    var = ViewModels().info_summ_product_in_basket(info_chek, summ_product)
    if var == 'Оплата':
        payment(clients_code, pay_r, summ_product)
    elif var == 'Повернутись до покупок':
        pass
    elif var == 'Видалити позиції':
        dell_position(pay_k)
    return discount


def dell_position(pay_k):
    var_choice = ViewModels().choose_position_for_del(pay_k)
    for i in var_choice:
        pay_k.pop(i)
    WorkDataJson().write_basket_file(pay_k)


def payment(clients_code, pay_r, summ_tovar):
    msgbox("Відскануйте QR код для оплати", image='images\\56.gif')
    pay = buttonbox("Пройшла оплата чи ні?", 'Pay', ['Ok', 'No'])
    if pay == "Ok":
        if clients_code in pay_r:
            pay_r[clients_code]['Сума'] = pay_r[clients_code]['Сума'] + summ_tovar
            WorkDataJson().write_clients_baza_file(pay_r)
        msgbox("Оплата пройшла успішно, Приємного", image='images\\Cjey.gif')
        del_cosh = {}
        WorkDataJson().write_basket_file(del_cosh)
        choice = "Відміна"
        return choice

    else:
        time.sleep(5)
        del_cosh = {}
        WorkDataJson().write_clients_baza_file(del_cosh)
        msgbox("Термін очікування вичерпано, вас поставлено на лічильник, наші люди йдуть до вас ,АТБ")
        choice = "Відміна"
        return choice


def loginPersonal():
    choice_login = multenterbox("Введіть логін та пароль", "CoffeeShop", ["Логін", "Пароль"])
    data = WorkDataJson().read_staff_file()
    if choice_login[0] == data.get(choice_login[0])["Login"]:
        if int(choice_login[1]) == data.get(choice_login[0])["Password"]:
            return personal_do()
        else:
            msgbox("Не вірний пароль", image='images\giphy.gif')
    else:
        msgbox("Такого користувача не знайдено", image='images\giphy.gif')


def personal_do():
    choice = ViewModels().view_personal_menu()
    if choice == 'Склад':
        storage()
    elif choice == 'Головна':
        return 'Головна'
    else:
        personal_do()


def product():
    name = ViewModels().add_product_personal()
    if name == 'Назад':
        return storage()
    list_product = multenterbox("Введіть параметри продукту", "Product", ["Назва", "Ціна", "Валюта", "Кількість"])
    type_prod = list_product[0]
    price = float(list_product[1])
    currency = list_product[2]
    count_prod = int(list_product[3])
    data = WorkDataJson().read_menu_file()
    if name in data:
        data[name].update({type_prod: {"Назва": type_prod, "Ціна": price, "Валюта": currency, "Кількість": count_prod}})
    else:
        data[name] = {type_prod: {"Назва": type_prod, "Ціна": price, "Валюта": currency, "Кількість": count_prod}}
    WorkDataJson().write_menu_file(data)


def change(do):
    while True:
        data = WorkDataJson().read_menu_file()
        choose_del = ViewModels().change_prod_personal(do)
        if do == 'Додати':
            data.get(choose_del[0]).get(choose_del[1])['Кількість'] += int(choose_del[2])
        elif do == 'Відняти':
            data.get(choose_del[0]).get(choose_del[1])['Кількість'] -= int(choose_del[2])
        WorkDataJson().write_menu_file(data)
        return 'ok'


def storage():
    data = WorkDataJson().read_menu_file()
    smakol_count = [dat for dat in data['Смаколики']]
    kava_count = [dat for dat in data['Кава']]
    smakol = [data['Смаколики'][i]['Кількість'] for i in smakol_count]
    kava = [data['Кава'][i]['Кількість'] for i in kava_count]

    kava_pars = []
    smakol_pars = []

    for i in range(len(smakol_count)):
        kava_pars.append('\n'+kava_count[i] + ' = ' + str(kava[i]) + 'шт')
        smakol_pars.append(smakol_count[i] + ' = ' + str(smakol[i]) + 'шт')

    for i in range(len(kava_pars)):
        pars = len(kava_pars[i])

        if pars < 18:
            result = 18 - len(kava_pars[i])
            kava_pars[i] += ' ' * result

    all_pars = []

    for i in range(len(kava_pars)):
        all_pars.append(kava_pars[i] + ' '*10 + smakol_pars[i])

    global magic
    magic = ' '.join([i for i in all_pars])
    choose = buttonbox(f"{magic}", 'Склад', ['Назад', 'Додати товар', 'Відняти товар', 'Головна'])

    if choose == 'Назад':
        return personal_do()
    elif choose == 'Додати товар':
        change('Додати')
    elif choose == 'Відняти товар':
        change('Відняти')
    elif choose == 'Головна':
        return 'Ok'


def all_info():
    pay_r = WorkDataJson().read_basket_file()
    summ_tovar = 0.0
    info_chek = ''
    for txt in pay_r:
        info_chek += f'{txt} - {pay_r.get(txt).get("Ціна")} {pay_r.get(txt).get("Валюта")}\n'
        summ_tovar += pay_r.get(txt).get("Ціна")
    info_chek += f'\nЗагальна сума покупки: {summ_tovar}'
    msgbox(info_chek, "info")
