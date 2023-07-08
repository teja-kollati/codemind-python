def findsmallnumbers(List,n):
    count = 0
    for i in List:
        if i < n:
            count += 1
    return count
n = int(input())
List = list(map(int,input().split()))
for i in List:
    print(findsmallnumbers(List,i),end = ' ')