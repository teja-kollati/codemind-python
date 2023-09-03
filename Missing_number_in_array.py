t = int(input())
while t > 0:
    n = int(input())
    List = list(map(int,input().split()))
    for i in range(1,n + 1):
        if i not in List:
            print(i)
            break;
    t -= 1