# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

for ind in range(1,10):

    dir_path = os.path.join(os.getcwd(), 'dir_'+str(ind))

    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('Такая директория уже существует')

for ind in range(1, 10):
    dir_path = os.path.join(os.getcwd(), 'dir_'+str(ind))
    if os.path.exists(dir_path):
        os.rmdir(dir_path)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

mypath = os.getcwd()

onlydirectories = [f for f in os.listdir(mypath) if os.path.isdir(os.path.join(mypath, f))]

print(onlydirectories)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil

file_name = os.path.basename(__file__)

shutil.copy(file_name, file_name+'.dupl')
