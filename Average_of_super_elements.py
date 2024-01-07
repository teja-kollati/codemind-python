def count(n,List):
    c = 0
    for i in List:
        if i == n:
            c += 1
    return c

n = int(input())
List = list(map(int,input().split()))
l = []
for i in List:
    if i == count(i,List):
        l.append(i)
if len(l) == 0:
    print('-1')
else:
    print("{:.2f}".format(sum(set(l))/len(set(l))))