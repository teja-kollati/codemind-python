n = int(input())
m = int(input())
l = []
for i in range(1,n + 1):
    List = list(map(int,input().split()))
    l.append(sum(List))
print(sum(l))