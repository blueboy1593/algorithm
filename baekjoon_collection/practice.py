aa = [ [0]*5 for _ in range(5) ]
print(aa)
aa[1][1] = [1,2,3]
aa[4][4] = [2,3]
print(aa)
aa[2][3] = aa[1][1]
aa[1][2] = aa[4][4]
print(aa)
aa[1][1] = 0
aa[4][4] = 0
print(aa)