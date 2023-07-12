n = int(input())
while n > 0:
    st = input()
    if st != st[::-1]:
        print("NO")
    else:
        if len(st)%2 == 0:
            print("YES EVEN")
        else:
            print("YES ODD")
    n -= 1