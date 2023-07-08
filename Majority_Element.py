def findcount(List,n):
    count = 0
    for i in List:
        if i == n:
            count += 1
    return count
n = int(input())
List = list(map(int,input().split()))
Dict = {}
for i in List:
    Dict[i] = findcount(List,i)
max_key = max(Dict, key = Dict.get)
print(max_key)