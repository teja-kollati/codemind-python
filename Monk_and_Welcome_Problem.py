n = int(input())
List1 = list(map(int,input().split()))
List2 = list(map(int,input().split()))
List = []
for i in range(0,n):
    List.append(List1[i] + List2[i])
for i in List:
    print(i,end = ' ')