# 3. Пользователь подаёт на ввод список из чисел, необходимо вывести список, состоящий только из чётных чисел (append)

#задание 3
num = input("Введите список числа через пробел : ").split() # Пишем список чисел
spisok_chetnih_chisel= []#Создаем пустой список для хранения четных чисел
for number in num: # Проходим по каждому элементу списка введенных чисел
    number = int(number) # Преобразуем элемент в число
    if number % 2 == 0: # Проверяем, является ли число четным
        spisok_chetnih_chisel.append(number) # Если число четное, добавляем его в список четных чисел
print("Список четных чисел:", spisok_chetnih_chisel) # Выводим список четных чисел