list1 = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
new = []
for i in list1:
    present=False
    for j in new:
        if j == i:
            present=True
    if not present:
        new+= [i]
print(new)

        