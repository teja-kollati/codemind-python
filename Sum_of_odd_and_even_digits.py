n = int(input())
List = list(map(int,input().split()))
even_sum = 0
odd_sum = 0
for i in range(0,n):
    if i % 2 == 0:
        even_sum += List[i]
    else:
        odd_sum += List[i]
if even_sum - odd_sum == 0:
    print('YES')
else:
    print('NO')