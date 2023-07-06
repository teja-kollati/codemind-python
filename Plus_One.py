n = int(input())
arr = list(map(int,input().split()))
num = 0
for i in range(0,n):
    num = num * 10 + arr[i]
num += 1
l = []
while num > 0:
    l.append(num % 10)
    num //= 10
for i in range(len(l) - 1,-1,-1):
    print(l[i],end = ' ')