'''
Нужно реализовать класс StackMax,который поддерживает
операцию определения максимума среди всех элементов в стеке.
'''


class StackMax:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        print('error')

    def get_max(self):
        if self.items:
            print(max(self.items))
        else:
            print('None')


stack = StackMax()
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

# Time: 103ms, Memory: 4.16Mb
