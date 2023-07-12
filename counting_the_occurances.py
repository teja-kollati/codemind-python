s = input()
c = input()
count = 0
for i in s:
    if c == i:
        count += 1
if count == 0:
    print(-1)
else:
    print(count)