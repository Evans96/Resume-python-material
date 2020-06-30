import numpy as n

x = int(input("state level of pascals triangle: "))
s = n.zeros((x + 1, x + 1))
s[:, 0] = 1
p = 0
while p < x:
    f = 0
    p = p + 1
    while f < x:
        f = f + 1
        s[p, f] = s[p - 1, f] + s[p - 1, f - 1]
print(s)
