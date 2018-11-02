# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os

def current_dir():
    current_dir = os.getcwd()
    print(f'Сейчас Вы находитесь в папке {current_dir}')
    dir_name = input('Введите имя имя папки для перехода: ')

    if not dir_name:
        print("Необходимо указать имя папки для перехода")
        return

    if dir_name != '..':
        dir_path = os.path.join(os.curdir, dir_name)
    else:
        if os.getcwd() != base_dir:
            dir_path = '..'
        else:
            print('Запрещен выход из рабочей папки')
            return

    if os.path.exists(dir_path):
        os.chdir(dir_path)
        print(os.getcwd())
        print('Успешно перешел')

def copy_dir():
    pass

def remove_dir():
    dir_name = input('Введите имя удаляемой папки: ')

    if not dir_name:
        print("Необходимо указать имя удаляемой папки")
        return

    dir_path = os.path.join(os.getcwd(), dir_name)

    if os.path.exists(dir_path):
        os.rmdir(dir_path)
        print('Успешно удалено')
    else:
        print(f"Не могу удалить не существующую папку")

def list_dir():
    current_dir = os.getcwd()
    print(f'Сейчас Вы находитесь в папке {current_dir}.')

    onlydirectories = [f for f in os.listdir(os.curdir) if os.path.isdir(os.path.join(os.curdir, f))]
    onlyfiles = [f for f in os.listdir(os.curdir) if os.path.isfile(os.path.join(os.curdir, f))]

    if onlydirectories:
        print('Папки:')
        for el in onlydirectories:
            print(el)

    if onlyfiles:
        print('Файлы:')
        for el in onlyfiles:
            print(el)

    if not(onlydirectories and onlyfiles):
        print('Папка пуста')

def make_dir():

    dir_name = input('Введите имя создаваемой папки: ')

    if not dir_name:
        print("Необходимо указать имя создаваемой папки")
        return

    dir_path = os.path.join(os.getcwd(), dir_name)

    try:
        os.mkdir (dir_path)
        print ( f'Папка {dir_name} успешно создана')
    except FileExistsError:
        print ( f'Папка {dir_name} уже существует')

do_func = {
        '1': current_dir,
        '3': remove_dir,
        '2': list_dir,
        '4': make_dir
    }

do = ''

base_dir = os.getcwd()

while do !='q':
    print("Я умею:")
    print(" [1] - переходить в указанную папку")
    print(" [2] - просматривать содержимое текущей папки")
    print(" [3] - удалять папку")
    print(" [4] - создавать папку")
    do = input("Укажите номер действия: ")

    if do in do_func:
        do_func[do]()
    elif do == 'q':
        print('До свидания!')
    else:
        print('Указан неверный номер действия')
