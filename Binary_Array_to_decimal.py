n = int(input())
List = list(map(int,input().split()))
num = 0
for i in range(0,n):
    if List[i] == 1:
        num += (2**(n - i - 1))
print(num)