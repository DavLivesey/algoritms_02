'''
Дана матрица.
Нужно написать функцию, которая для элемента возвращает всех его соседей.
Соседним считается элемент, находящийся от текущего на одну ячейку влево,
вправо, вверх или вниз. Диагональные элементы соседними не считаются.
'''

count_strings = int(input())
count_columns = int(input())
matrix = []
for i in range(count_strings):
    row = list(map(int, input().split(' ')))
    matrix.append(row)
x = int(input())
y = int(input())
answer = []
if x > 0:
    answer.append(matrix[x-1][y])
if y > 0:
    answer.append(matrix[x][y-1])
if x < count_strings - 1:
    answer.append(matrix[x+1][y])
if y < count_columns - 1:
    answer.append(matrix[x][y+1])
answer.sort()
print(' '.join(repr(i) for i in answer))

# Time: 143ms, Memory: 14.88Mb
