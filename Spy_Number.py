n = int(input())
product = 1
Sum = 0
while n > 0:
    digit = n % 10
    product *= digit
    Sum += digit
    n //= 10
if product == Sum:
    print("Spy Number")
else:
    print("Not Spy Number")