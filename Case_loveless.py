'''
Вася размышляет, что бы такое из списка не делать.
Но, кажется, все пункты очень важные!
Вася решает загадать число и удалить дело, которое идёт под этим номером.
Список дел представлен в виде односвязного списка.
Напишите функцию solution, которая принимает на вход голову списка
и номер удаляемого дела и возвращает голову обновлённого списка.
'''


def solution(node, idx) -> None:
    head = node
    if idx == 0:
        node = head.next_item
        return node
    while idx > 1:
        node = node.next_item
        idx -= 1
    tmp = node.next_item.next_item
    node.next_item = tmp
    return head

# Time: 44ms, Memory: 5.50Mb
