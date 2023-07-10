def gcd(a,b):
    while a!= b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
n = int(input())
List = list(map(int,input().split()))
result = List[0]
for i in range(1,n):
    result = gcd(result,List[i])
print(result)