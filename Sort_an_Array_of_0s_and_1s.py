n = int(input())
my_list = list(map(int,input().split()))
sorted_list = sorted(my_list)
for i in range(0,n):
    print(sorted_list[i],end = ' ')