n = int(input())
List = list(map(int,input().split()))
l = []
for i in range(n - 1,n//2 - 1,-1):
    l.append(List[i])
for i in range(0,n//2):
    l.append(List[i])
for i in l:
    print(i,end = ' ')