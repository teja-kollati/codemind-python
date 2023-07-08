n = int(input())
if(n > 0):
    n = n
    num = 0
    while n > 0:
        digit = n % 10
        num = num * 10 + digit
        n //= 10
    print(num)
else:
    n = -n
    num = 0
    while n > 0:
        digit = n % 10
        num = num * 10 + digit
        n //= 10
    print(-num)