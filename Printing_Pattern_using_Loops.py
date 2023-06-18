n = int(input())
for i in range(1,2 * n):
    temp = n
    for j in range(1,2*n):
        print(temp,end = ' ')
        if j < i:
            temp -= 1
        if j > (2*n - 1 - i):
            temp += 1
    print()