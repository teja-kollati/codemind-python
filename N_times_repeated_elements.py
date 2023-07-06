def findcount(List,n):
    count = 0
    for i in List:
        if i == n:
            count += 1;
    return count
    
size = int(input())
List = list(map(int,input().split()))
n = int(input())
l = []
for i in List:
    if findcount(List,i) == n and i not in l:
        l.append(i)
if len(l) == 0:
    print(-1)
else:
    for i in l:
        print(i,end = ' ')