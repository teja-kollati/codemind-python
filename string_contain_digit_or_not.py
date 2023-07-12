st = input()
count = 0
for i in st:
    if i in "1234567890":
        count += 1
if count == 0:
    print("Doesn't contain digit")
else:
    print("Contains {} digit".format(count))