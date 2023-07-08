def fact(n):
    fact = 1
    for i in range(1,n + 1):
        fact *= i
    return fact
n = int(input())
temp = n
num = 0
while temp > 0:
    digit = temp % 10
    num += fact(digit)
    temp //= 10
if num == n:
    print('The number {} is a strong number'.format(n))
else:
    print('The number {} is not a strong number'.format(n))