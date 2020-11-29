'''
Реализуйте класс StackSet, который хранит только уникальные элементы.
При этом операция добавления элемента в стек должна выполняться за O(1).
'''


class StackSet:
    def __init__(self):
        self.items = []
        self.max_list = []
        self.unique_stack = set()

    def is_empty(self):
        return self.items == []

    def push(self, item):
        if item not in self.unique_stack:
            self.items.append(item)
            self.unique_stack.add(item)
        if self.max_list == [] or self.max_list[-1] <= item:
            self.max_list.append(item)

    def pop(self):
        if self.items:
            item = self.items[-1]
            self.unique_stack.remove(item)
            if item == self.max_list[-1]:
                self.max_list.pop()
            return self.items.pop()
        print('error')

    def get_max(self):
        if self.items:
            print(self.max_list[-1])
        else:
            print('None')

    def size(self):
        print(len(self.items))

    def peek(self):
        if self.items:
            print(self.items[-1])
        else:
            print('error')

    def print(self):
        print(' '.join(repr(element) for element in self.items))
        print(
            ''.join(repr(element) for element in self.unique_stack),
            ' unique'
        )


stack = StackSet()
count_actions = int(input())
for i in range(count_actions):
    method = input().split(' ')
    if method[0] == 'pop':
        stack.pop()
    elif method[0] == 'get_max':
        stack.get_max()
    elif method[0] == 'push':
        num = int(method[1])
        stack.push(num)
    elif method[0] == 'size':
        stack.size()
    elif method[0] == 'peek':
        stack.peek()
    elif method[0] == 'print':
        stack.print()


# Time: 98ms, Memory: 4.20Mb
