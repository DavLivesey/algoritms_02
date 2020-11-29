'''
Напишите код для решения задачи про поиск кружков,
которые посещает хотя бы один ученик. Ваше решение должно задействовать
O(1) дополнительной памяти
(то есть помимо памяти, выделенной под массив visited_optional_courses)
'''

courses = (input() for i in range(int(input())))
optional_courses = []
for i in courses:
    if i not in optional_courses:
        optional_courses.append(i)

for i in optional_courses:
    print(i)

# Time: 0.673s, Memory: 4.21Mb
