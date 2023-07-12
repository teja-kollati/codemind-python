n = int(input())
for i in range(0,n):
    st = input()
    for i in st:
        if i not in "0123456789":
            print(False)
            break
    else:
        print(True)