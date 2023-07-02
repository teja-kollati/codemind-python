n = int(input())
l = list(map(int,input().split()))
num = 0
for i in range(0,n):
    num += l[i] * 2**(n - i - 1)
print(num)