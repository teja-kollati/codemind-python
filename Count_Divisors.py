a,b,c = map(int,input().split())
l = []
for i in range(a,b + 1):
    if i % c == 0:
        l.append(i)
print(len(l))