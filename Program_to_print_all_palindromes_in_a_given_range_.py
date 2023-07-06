def ispalindrome(n):
    temp = n
    num = 0
    while temp > 0:
        digit = temp % 10
        num = num * 10 + digit
        temp //= 10
    if num == n:
        return 1
    else:
        return 0
a = int(input())
b = int(input())
for i in range(a,b):
    if ispalindrome(i) == 1:
        print(i,end = ' ')