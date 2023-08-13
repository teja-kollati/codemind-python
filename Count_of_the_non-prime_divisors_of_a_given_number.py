def isprime(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        for i in range(2,n//2 + 1):
            if n % i == 0:
                return 0
                break
        return 1

n = int(input())
l = []
for i in range(1,n + 1):
    if n % i == 0:
        if isprime(i) == 0:
            l.append(i)
print(len(l))