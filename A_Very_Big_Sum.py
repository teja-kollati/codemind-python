n = int(input())
arr = list(map(int,input().split()))
SUM = 0
for i in range(0,n):
    SUM += arr[i]
print(SUM)