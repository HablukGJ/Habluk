# Уровень C
# Хаблюк Григорий ИИ-72
# Задача 1
def create_triangle(size, symbol):
    matrix = []
    row_index = 0
    for i in range(size):
        row = []
        spaces = (size - (row_index * 2 + 1)) // 2
        insight_space = size - spaces * 2 - 2
        # print(f'Spaces: {spaces}\ninsight_space: {insight_space}')
        if row_index == 0:
            for space in range(spaces):
                row.append(' ' * len(symbol))
            row.append(symbol)
            for space in range(spaces):
                row.append(' ' * len(symbol))
        elif spaces == 0:
            for j in range(size):
                row.append(symbol)
        elif spaces < 0:
            for j in range(size):
                row.append(' ' * len(symbol))
        else:
            for space in range(spaces):
                row.append(' ' * len(symbol))
            row.append(symbol)
            for space in range(insight_space):
                row.append(' ' * len(symbol))
            row.append(symbol)
            for space in range(spaces):
                row.append(' ' * len(symbol))
        matrix.append(row)
        row_index += 1
    for row in matrix:
        for element in row:
            print(element, end='\t')
        print()

while True:
    try:
        size = int(input("Введите размер в виде нечетного положительного числа: "))
    except:
        print("Пожалуйста, введите число")
        continue
    if size < 1 or size % 2 == 0:
        print("Пожалуйста, введите полодительное нечетное число")
        continue
    symbol = input("Введите символ для заполнения: ")
    create_triangle(size, symbol)


# Задача 2
while True:
    try:
        number = int(input("Введите число: "))
    except:
        print('введите число')
        continue
    space = input("Введите промежуток в формате: a b").split(' ')
    if len(space) != 2:
        print('введите два числа')
        continue
    elif int(space[0]) > int(space[1]):
        print('первое число должно быть меньше или равно второму')
        continue


is_included = False

for i in range(int(space[0]), int(space[1]) + 1):
    if number == i:
        print('принадлежит')
        is_included = True

if is_included:
    print('принадлежит')
else:
    print('не принадлежит')

# Задача 3
import random
while True:
    try:
        n = int(input("Введите количество чисел, необходимых для генерации: "))
        max_number = int(input("Введите максимальное значение: "))
        if n < 0 or max_number < 0:
            print("Пожалуйста, введите положительное")
            continue
        else:
            break
    except:
        print("Пожалуйста, введите число")
        continue


matrix_size = 0
while matrix_size ** 2 < n:
    matrix_size += 1

matrix = [[random.randint(0, max_number) for i in range(matrix_size)]for j in range(matrix_size)]
for row in matrix:
    for element in row:
        print(element, end='\t')
    print()

matrix_2 = [[0 for j in range(matrix_size)]for i in range(matrix_size)]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        try:
            matrix_2[i][j - 1] = matrix[i][j]
        except:
            matrix_2[i][matrix_size - 1] = matrix[i][j]

for row in matrix_2:
    for element in row:
        print(element, end='\t')
    print()
