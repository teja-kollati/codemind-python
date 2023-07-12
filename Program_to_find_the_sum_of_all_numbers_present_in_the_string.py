st = input()
l = []
for i in st:
    if i in "123456789":
        l.append(int(i))
print(sum(l))