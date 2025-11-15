from datetime import datetime
import re

# Создаем регулярные выражения
NAME_PATTERN = re.compile(r'^[А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+$')
EMAIL_PATTERN = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
PHONE_PATTERN = re.compile(r"^(\+7|8)\s?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}$")
DATE_PATTERN = re.compile(r'\d\d/\d\d/\d{4}')

selected_ingredients = {}

# Создаем словари с меню
menu_kids = {
    "Пицца KIDS 700г": 999,
    "Котлета куриная 300г": 299,
    "Картофельное пюре 250г": 299,
    "Куриный суп 300г": 399,
    "Пельмени 300г": 599,
    "Чизкейк 70г": 199,
    "Шоколадный фондан 70г": 249
}
bar_menu_kids = {
    "Яблочный сок 100г": 149,
    "Апельсиновый сок 100г": 199
}
menu_adult = {
    "Пицца Маргарет 1000г": 1299,
    "Котлета куриная 600г": 399,
    "Картофельное пюре 250г": 399,
    "Том ям 700г": 699,
    "Пельмени 300г": 599,
    "Чизкейк 70г": 199,
    "Шоколадный фондан 70г": 249,
}
bar_menu_adult = {
    "Яблочный сок 100г": 149,
    "Апельсиновый сок 100г": 199
}

while True:
    name = input("Введите свое ФИО: ")
    if not NAME_PATTERN.match(name):
        print('Введите ФИО корректно')
        continue
    else:
        break

while True:
    email = input("Введите почту: ")
    if not EMAIL_PATTERN.match(email):
        print('Введите почту корректно')
        continue
    else:
        break

while True:
    phone = input("Введите телефон: ")
    if not PHONE_PATTERN.match(phone):
        print('Введите телефон корректно')
        continue
    else:
        break

while True:
    date_of_birth = input("Введите датц рождения (ДД/ММ/ГГГГ): ")
    if not DATE_PATTERN.match(date_of_birth):
        print('Введите дату корректно')
        continue
    else:
        try:
            datetime(int(date_of_birth.split('/')[2]), int(date_of_birth.split('/')[1]), int(date_of_birth.split('/')[0]))
        except:
            print("Введите существующую дату")
            continue
        age = datetime.now().year - int(date_of_birth.split('/')[2])
        break

# Декоратор
def select(func):
    def output_func(age):
        print('-' * 100)
        func(age)
        print('-' * 100)
    return output_func


@select
def show_bar_menu(age):
    if age < 10:
        print("Тебе доступно барное детское меню:")
        j = 1
        for i in bar_menu_kids:
            print(f'{j}. {i}{" " * (100 - len(i) - len(str(bar_menu_kids[i])))}{bar_menu_kids[i]}')
            j += 1
    else:
        print("Тебе доступно барное меню для взрослых: ")
        j = 1
        for i in bar_menu_adult:
            print(f'{j}. {i}{" " * (100 - len(i) - len(str(bar_menu_adult[i])))}{bar_menu_adult[i]}')
            j += 1

@select
def show_menu(age):
    if age < 10:
        print("Тебе доступно детское меню:")
        j = 1
        for i in menu_kids:
            print(f'{j}. {i}{" " * (100 - len(i) - len(str(menu_kids[i])))}{menu_kids[i]}')
            j += 1

    else:
        print("Тебе доступно взрослое меню:")
        j = 1
        for i in menu_adult:
            print(f'{j}. {i}{" " * (100 - len(i) - len(str(menu_adult[i])))}{menu_adult[i]}')
            j += 1

@select
def show_total(age = 0):
    total = 0
    for i in selected_ingredients:
        total += selected_ingredients[i]

    print("ЧЕК: ")
    for i in selected_ingredients:
        print(f"{i}{' ' * (100 - len(i) - len(str(selected_ingredients[i])))}{selected_ingredients[i]}")
    print(f"ВСЕГО: {total} руб.")

def order_menu(age):
    print('Приветствуем вас в нашей пиццерии! Что пожелаете заказать?')
    while True:

        show_menu(age=age)

        while True:
            try:
                order = int(input("Введите номер заказа (0 для вывода чека): "))
                if order < 0 or order > 7:
                    print('Введите существующий номер')
                    continue
                elif order == 0:
                    show_total(age)
                    exit(0)
                else:
                    if age < 10:
                        selected_ingredients[list(menu_kids)[order - 1]] = menu_kids[list(menu_kids)[order - 1]]
                    else:
                        selected_ingredients[list(menu_adult)[order - 1]] = menu_adult[list(menu_adult)[order - 1]]
                    break
            except Exception as e:
                print(e)
                continue

        show_bar_menu(age=age)

        while True:
            try:
                order = int(input("Введите номер заказа (0 для вывода чека): "))
                if order < 0 or order > 2:
                    print('Введите существующий номер')
                    continue
                elif order == 0:
                    show_total(age)
                    exit(0)
                else:
                    if age < 10:
                        selected_ingredients[list(bar_menu_kids)[order - 1]] = bar_menu_kids[list(bar_menu_kids)[order - 1]]
                    else:
                        selected_ingredients[list(bar_menu_adult)[order - 1]] = bar_menu_adult[list(bar_menu_adult)[order - 1]]
                    break
            except Exception as e:
                print(e)
                continue


order_menu(age)