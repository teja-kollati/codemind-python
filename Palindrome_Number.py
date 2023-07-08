t = int(input())
while t > 0:
    n = int(input())
    temp = n
    num = 0
    while temp > 0:
        digit = temp % 10
        num = num * 10 + digit
        temp //= 10
    if num == n:
        print(True)
    else:
        print(False)
    t -= 1