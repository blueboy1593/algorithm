dwarf = []
for _ in range(9):
    dwarf.append(int(input()))

sumsum = sum(dwarf)
a = 0
for i in range(9):
    for j in range(i+1, 9):
        if dwarf[i] + dwarf[j] == sumsum - 100:
            a = dwarf[i]
            b = dwarf[j]
            break
    if a:
        break
dwarf.remove(a)
dwarf.remove(b)
dwarf.sort()
for k in range(7):
    print(dwarf[k])