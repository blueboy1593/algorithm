N = int(input())

tyle_list = list(map(int, input().split()))

def findhab(i, j):
    global leng, maxhab
    a = tyle_list[i]
    b = tyle_list[j]
    cha = b - a
    hab = 0
    c = b + cha
    for k in range(j + 1, leng):
        if tyle_list[k] == c: # 처음에 3개 이상으로 존재할 수 있는지 검사.
            hab = a + b + c
            d = c + cha
            while True: # 3개가 확보 되었을때 추가로 받을 수 있는지 검사. 리스트 내 숫자 검색하다가 기준값 넘어가면 리턴.
                if tyle_list[-1] < d:
                    if hab > maxhab:
                        maxhab = hab
                    return
                for l in range(k + 1, leng):
                    if tyle_list[l] == d:
                        hab += d
                        d += cha
                        k = l
                        break
                    elif tyle_list[l] > d:
                        if hab > maxhab:
                            maxhab = hab
                        return
        elif tyle_list[-1] < c:
            return
        elif tyle_list[k] > c:
            return

hab_list = []
maxhab = 0
leng = len(tyle_list)

for i in range(leng):
    for j in range(i + 1, leng):
        findhab(i, j)

print(maxhab)