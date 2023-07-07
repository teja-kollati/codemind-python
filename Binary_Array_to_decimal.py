n = int(input())
List = list(map(int,input().split()))
num = 0
for i in range(0,n):
    num += List[i]*(2**(n - i - 1))
print(num)