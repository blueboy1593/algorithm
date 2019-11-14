from pprint import pprint
aa = [ [0]* 10 for _ in range(10) ]

for j in range(10):
    aa[j][j] = 1
    aa[j][6] = 1
pprint(aa)
bb = list(zip(*aa))

def change(arr):
    for i in range(len(arr)):
        arr[i].reverse()
    return arr
change(aa)
pprint(aa)