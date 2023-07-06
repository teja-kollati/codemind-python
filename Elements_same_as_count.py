def findcount(List,n,key):
    count = 0
    for i in List:
        if key == i:
            count += 1
    return count
n = int(input())
List = list(map(int,input().split()))
l = []
for i in List:
    if findcount(List,n,i) == i and i not in l:
        l.append(i)
if len(l) == 0:
    print(-1)
else:
    for i in l:
        print(i,end = ' ')