def reverse(n):
    num = 0
    while n > 0:
        num = num * 10 + (n % 10)
        n //= 10
    return num
def ispalindrome(n):
    if reverse(n) == n:
        return 1
    else:
        return 0
n = int(input())
while True:
    n += reverse(n)
    if ispalindrome(n) == 1:
        print(n)
        break