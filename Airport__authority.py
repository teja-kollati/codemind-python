n = int(input())
l = []
for i in range(1,n + 1):
    a = int(input())
    l.append(a)
t = int(input())
price = 0
for i in l:
    if i <= t:
        price += 1
    else:
        price += 2
print(price)