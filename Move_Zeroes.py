n = int(input())
List = list(map(int,input().split()))
l = []
for i in range(0,n):
    if List[i] != 0:
        l.append(List[i])
for i in range(len(l) - 1, n - 1):
    l.append(0)
for i in range(0,n):
    print(l[i],end = ' ')