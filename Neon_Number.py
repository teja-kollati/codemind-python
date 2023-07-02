def digit_sum(num):
    digits = []
    while num > 0:
        digit = num % 10
        digits.append(digit)
        num = num // 10
    return sum(digits)
n = int(input())
square = n*n
if(digit_sum(square) == n):
    print("Neon Number")
else:
    print("Not Neon Number")