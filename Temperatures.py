n = int(input())
List = list(map(int,input().split()))
l = []
for i in range(0,n):
    for j in range(i,n):
        if List[i] < List[j]:
            l.append(j - i)
            break
    else:
        l.append(0)
for i in l:
    print(i,end = ' ')