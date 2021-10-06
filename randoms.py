# testing random
import random
from collections import Counter


def randomfunc():
    a = random.random()
    print(a, end=', ')
    print(int(a * 10), end='; ')
    return int(a * 10)


list1 = []
x = 0
while x < 10:
    list1.append(random.randint(1, 9))
    x = x + 1
print(list1, end=', ')
print(Counter(list1), "\n")


list2 = []
x = 0
while x < 10:
    list2.append(randomfunc())
    x = x + 1
print(list2)
print(Counter(list2))
