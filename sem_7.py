# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы используется множество раз и вы не 
# хотите ничего сломать): 
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.

# Решение 1: 

# def transformation(values):
#     return values

# values = [1, 23, 42, "asdfg"]
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#     print("ok")
# else:
#     print("fail")

# Решение 2: 
# transformation = lambda x: x
# values = [1, 23, 42, "asdfg"]
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#     print("ok")
# else:
#     print("fail")

# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь.
#  Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту, по которой вращается самая далекая 
# планета. Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные спутники были были запущены на
# круговые орбиты. Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита 
# представляет из себя кортеж из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины 
# полуосей эллипса. При решении задачи используйте списочные выражения. Подсказка: проще всего будет найти эллипс в два шага: сначала 
# вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такую  площадь. Гарантируется, что самая далекая планета 
# ровно одна

# Ввод:

# РЕШЕНИЕ:
# orbits = [(1, 3), (2.5, 77), (7, 2), (6, 6), (4, 3)]

# def find_farthest_orbit(orbits):
#     s_orbits = {}
#     for a,b in orbits:
#         if a != b:
#             s_orbits[a * b] = a,b
#     return s_orbits[max(s_orbits)]

# print(find_farthest_orbit(orbits))

# Решение (препод)
# def find_fathest_orbit(orbits):
# max_area = 0
# i_orbit = 0
# for i, (a, b) in enumerate(orbits): # (0, (1, 3))
# if a != b and (area := a * b) > max_area:
# max_area = area
# i_orbit = i
#
# return orbits[i_orbit]

# Решение 2 (препод)
# def find_farthest_orbit(orbits):
# return max(orbits, key=lambda x: (x[0] != x[1]) * x[0] * x[1])

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3), (100, 100)]
# print(*find_farthest_orbit(orbits))

# Задача 2:

# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики,
#  и возвращают True, если это так. Если значение характеристики для разных объектов отличается - то False. Для пустого набора объектов,
#  функция должна возвращать True. Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
# Ввод: Вывод:


# def same_by(func,iter):
#     if iter:
#         for item in iter:
#             if func(item):
#                 return False
#             return True
#     else: return True

# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
#     print("same")
# else:
#     print("different")

# РЕШЕНИЕ ПРЕПОДА:

# def same_by(characteristic, objects):
#     lst = []
#     for val in objects:
#         lst.append(characteristic(val))
#     print(lst)
#     return all(item == lst[0] for item in lst)

# values = [0, 3, 10, 6]
# if same_by(lambda x: x % 2, values):
#     print("same")
# else:
#     print("different")