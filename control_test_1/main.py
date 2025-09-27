import numpy as np
import datetime

# Уровень C

# Задача 1

numbers = [1, 2, 100]
sum = 0
for i in numbers:
    sum += i
the_mean_number = sum / len(numbers)

a = np.array(numbers)
result = np.var(a)
print(f'Среднее значение: {the_mean_number}\n'
      f'Дисперсия: {result}')

# Задача 2

def round_to_the_biggest(number):
    if round(number) < number:
        return round(number) + 1
    else:
        return round(number)

alphabet = int(input('Введите колво символов в алфавите: '))
lines = int(input('Введите колво строк на странице: '))
letters = int(input('Введите колво символов в строке: '))
power = 0
while 2 ** power < alphabet:
    power += 1
all_letters_number = lines * letters * 2
bits = power * all_letters_number
print(f'Результат в битах: {bits}\n'
      f'Результат в байтах: {round_to_the_biggest(bits / 8)}\n'
      f'Результат в килобайтах: {round_to_the_biggest(bits / 8 / (2 ** 10))}\n'
      f'Результат в мегабайтах: {round_to_the_biggest(bits / 8 / (2 ** 20))}\n'
      f'Результат в гигабайтах: {round_to_the_biggest(bits / 8 / (2 ** 30))}\n'
      f'Результат в терабайтах: {round_to_the_biggest(bits / 8 / (2 ** 40))}\n')

# Задача 3

date = input('Введите дату (01.01.2000): ')
date = date.split('.')
for i in range(len(date)):
    date[i] = int(date[i])
try:
    datetime.date(int(date[2]), int(date[1]), int(date[0]))
    print('дата существует')
except:
    print('Даты не существует')
