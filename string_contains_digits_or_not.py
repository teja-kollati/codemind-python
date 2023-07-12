n = int(input())
while n > 0:
    st = input()
    for i in st:
        if i in "987654321":
            print("Yes")
            break;
    else:
        print("No")
    n -= 1