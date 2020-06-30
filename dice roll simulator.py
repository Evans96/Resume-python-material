def checker(self):
    c = 'true'
    try:
        int(self)
    except ValueError:
        c = 'false'
    return c



import random as r
import matplotlib.pyplot as plt
import numpy as n
x = input('how many dice would you like to roll? ')
l = input('how many sides does each dices have? ')
dice = checker(x)
side = checker(l)
array_creator = n.zeros((2, int(l)))
array_creator[0, :] = n.linspace(1, int(l), int(l))
n = 0
if side == 'true' and dice == 'true':
    while int(x) > n:
        p = r.randint(1, int(l))
        array_creator[1, p - 1] = array_creator[1, p - 1] + 1
        n = n + 1
    print(array_creator)
    plt.bar(array_creator[0, :], array_creator[1, :], )
    plt.xlabel('Number on dice')
    plt.ylabel('Number of times shown')
    plt.show()
