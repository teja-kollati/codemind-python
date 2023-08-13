n = int(input())
List = list(map(int,input().split()))
even = 0
odd = 0
for i in range(0,len(List)):
    if List[i]%2 == 0:
        even += 1
    else:
        odd += 1
print(even,odd)