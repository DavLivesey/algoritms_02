'''
На вход подается строка.
Нужно определить длину наибольшей подстроки,
которая не содержит повторяющиеся символы.
'''

string = input()
a = []
num = []
x = []
b = 0
for i in string:
    if i not in a:
        a.append(i)
        b = len(a)
        num.append(b)
    else:
        b = len(a) - a.index(i)
        x = a[(a.index(i)+1)::]
        a.clear()
        a.extend(x)
        a.append(i)
        num.append(b)
        b = 1
print(max(num))

# Time: 49ms, Memory: 4.22Mb
