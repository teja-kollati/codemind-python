n = int(input())
ar = list(map(int,input().split()))
sort = list(set(ar))
for i in sort:
    print(i,end = ' ')