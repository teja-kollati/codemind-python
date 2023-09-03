def isperfect(n):
    if n == 1:
        return 1
    for i in range(1,n//2 + 1):
        if i*i == n:
            return 1
    else:
        return 0
n = int(input())
List = list(map(int,input().split()))
l = []
for i in List:
    if isperfect(i) == 1:
        l.append(i)
print(sum(l))