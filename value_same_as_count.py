def count(List,n):
    c = 0
    for i in List:
        if i == n:
            c += 1
    return c
n = int(input())
List = list(map(int,input().split()))
l = []
for i in List:
    if count(List,i) == i:
        l.append(i)
print(len(set(l)))