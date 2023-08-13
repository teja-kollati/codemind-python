def add_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s
n = int(input())
Sum = add_digits(n)
while Sum > 9:
    n = Sum
    Sum = add_digits(n)
print(Sum)