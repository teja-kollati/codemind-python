ar1 = list(map(int,input().split()))
ar2 = list(map(int,input().split()))
alice = 0
bob = 0
for i in range(0,len(ar1)):
    if ar1[i] > ar2[i]:
        alice += 1
    elif ar1[i] < ar2[i]:
        bob += 1
print(alice,bob)