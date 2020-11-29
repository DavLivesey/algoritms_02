'''
Мама Васи хочет знать, что сын планирует делать и когда.
Помогите ей: напишите функцию solution,
определяющую индекс первого вхождения
передаваемого ей на вход значения в связном списке, если значение присутствует
'''


def solution(node, elem) -> int:
    value = ''
    index = 0
    while value != elem:
        value = node.value
        node = node.next_item
        index += 1
        if node.next_item == None:
            return -1
    return index - 1

# Time: 57ms, Memory: 7.02Mb
