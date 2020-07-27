drive = open("p.txt")
c = drive.read()
c = c.split()
n = len(c)
print(range(n))
s = 1
for d in range(n):
    for i in range(0, n - d - 1):
        print(i)
        if str(c[i])[0].lower() > str(c[i + 1])[0].lower():
            c[i], c[i + 1] = c[i + 1], c[i]

print(" ".join(c))
