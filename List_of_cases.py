'''
Васе нужно распечатать свой список дел на сегодня.
Помогите ему: напишите функцию, которая печатает все его дела.
Известно, что дел у Васи не больше
'''


def solution(node) -> None:
    while node is not None:
        print(node)
        node = node.next_item

# Time: 52ms, Memory: 6.75Mb
