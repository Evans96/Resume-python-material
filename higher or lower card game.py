import random as r

x = True
n = r.randint(0, 13)
score = 0
while x == True:
    c = r.randint(0, 13)
    while c == n:
        c = r.randint(0, 13)
    print('The current number is ', n, )
    ques = input(' higher or lower?')
    if ques == 'higher':
        x = bool(c > n)
        n = c
        if x == True:
            score = score + 1
            print('correct your correct score is', score)
    if ques == 'lower':
        x = bool(c < n)
        n = c
        if x == True:
            score = score + 1
            print('correct your correct score is', score)
print('you lose your final score is ', score)
