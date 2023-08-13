def isprime(n):
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return 0
            break
    return 1
t = int(input())
while t > 0:
    n = int(input())
    prime = []
    for i in range(n,0,-1):
        if isprime(i) == 1:
            prime.append(i)
            break
    for i in range(n,10000):
        if isprime(i) == 1:
            prime.append(i)
            break
    if (n - prime[0]) < (prime[1] - n):
        print(prime[0])
    elif (n - prime[0]) > (prime[1] - n):
        print(prime[1])
    else:
        print(prime[0])
    t -= 1