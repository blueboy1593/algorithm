import sys
sys.stdin = open("4366_input.txt", "r")

def binary(arr):
    get = 0
    for i in range(len(arr) - 1):
        get = (arr[i] + get) * 2
    get += arr[-1]
    return get

def triple(arr):
    get = 0
    for i in range(len(arr) - 1):
        get = (arr[i] + get) * 3
    get += arr[-1]
    return get

T = int(input())
for tc in range(1, T + 1):
    N2 = input()
    N3 = input()
    n2 = list(map(int, N2))
    n3 = list(map(int, N3))
    
    n2_list = []
    n3_list = []
    for i in range(len(n2)):
        n22 = n2[:]
        if n2[i] == 1:
            n22[i] = 0
        if n2[i] == 0:
            n22[i] = 1
        n2_list.append(n22)
    
    for i in range(len(n3)):
        for j in range(3):
            n33 = n3[:]
            if n3[i] != j:
                n33[i] = j
                n3_list.append(n33)
        # 아하 슬라이싱때문에 이미 추가한 인덱스까지 변하는구나.... 너무한거 아닌가....?
    
    n3_valuelist = []
    for sam in n3_list:
        n3_valuelist.append(triple(sam))
    
    for dul in n2_list:
        value = binary(dul)
        if value in n3_valuelist:
            result = value
            break
    
    print("#%d %s" %(tc, result))