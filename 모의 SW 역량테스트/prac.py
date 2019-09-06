aaa = [[1, 2], [2, 3], [3, 4]]
for a in aaa:
    print(a)
    if a[0] == 1 or a[0] == 2:
        aaa.remove(a)
print(aaa)