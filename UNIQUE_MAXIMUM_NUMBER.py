def findcount(List,n):
    count = 0
    for i in List:
        if i == n:
            count += 1
    return count
n = int(input())
List = list(map(int,input().split()))
l = []
for i in List:
    if findcount(List,i) == 1:
        l.append(i)
if len(l) == 0:
    print(-1)
else:
    print(max(l))