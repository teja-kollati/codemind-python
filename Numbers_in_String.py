st = input()
l = []
for i in st:
    if i in "1234567890":
        l.append(int(i))
print(sum(l))