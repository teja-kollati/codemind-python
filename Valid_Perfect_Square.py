t = int(input())
while t > 0:
    n = int(input())
    for i in range(1,n//2 + 1):
        if i*i == n:
            print(True)
            break
    else:
        print(False)
    t -= 1