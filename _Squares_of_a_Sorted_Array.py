n = int(input())
List = list(map(int,input().split()))
l = []
for i in List:
    l.append(i**2)
arr = sorted(l)
for i in arr:
    print(i,end = ' ')