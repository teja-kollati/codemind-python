def isprime(n):
    for i in range(2,n//2 + 1):
        if n % i == 0:
            return -1
            break
    else:
        return 1
n = int(input())
List = list(map(int,input().split()))
prime_product = 1
non_prime_product = 1
for i in List:
    if isprime(i) == 1:
        prime_product *= i
    else:
        non_prime_product *= i
print(abs(prime_product - non_prime_product))