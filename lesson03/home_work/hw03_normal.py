# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fibonacci_series = [1, 1]
    result = []

    for element in range(2, m):

        value = fibonacci_series[element-2]+fibonacci_series[element-1]
        fibonacci_series.append(value)
        if element >= n-1:
            result.append(value)

    return result

print(fibonacci(3,10))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    n = 1
    while n < len(origin_list):
        for i in range(len(origin_list) - n):
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
        n += 1

    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

# adults = filter(myFunc, ages)
#
# for x in adults:
#   print(x)

def filter_analog(method, values):
    for element in values:
        if method(element):
            yield element


adults = filter_analog(myFunc, ages)

for x in adults:
    print(x)

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

from collections import defaultdict

points = [[0, 0], [0, 1], [1, 0], [1, 1]]

vectors = defaultdict(list)

result = False

for i in range(len(points)):
    x1, y1 = points[i]
    for j in range(i + 1, len(points)):
        x2, y2 = points[j]
        vectors[(x2 - x1, y2 - y1)].append((i, j))

for vector, pairs in vectors.items():
    if len(pairs) > 1:
        result = True

print(result)



