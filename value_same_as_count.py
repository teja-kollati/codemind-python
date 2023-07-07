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
    if findcount(List,i) == i and i not in l:
        l.append(i)
print(len(l))