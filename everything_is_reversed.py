'''
Вася решил запутать маму —– делать дела в обратном порядке.
Список его дел теперь хранится в двусвязном списке.
Напишите функцию, которая вернёт список в обратном порядке.
'''


class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


def solution(node):
    head = None
    while node:
        tmp = node.next
        node.next = node.prev
        node.prev = tmp
        head = node
        node = node.prev
    return head

# Time: 45ms, Memory: 6.22Mb
