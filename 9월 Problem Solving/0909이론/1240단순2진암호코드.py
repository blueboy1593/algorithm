import sys
sys.stdin = open("1240_input.txt", "r")

T = int(input())

mydict = {}
mydict[0] = '0001101'
mydict[1] = '0011001'
mydict[2] = '0010011'
mydict[3] = '0111101'
mydict[4] = '0100011'
mydict[5] = '0110001'
mydict[6] = '0101111'
mydict[7] = '0111011'
mydict[8] = '0110111'
mydict[9] = '0001011'

print(mydict)

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    compare = '0'* M

    for _ in range(N):
        temp = input()
        if temp != compare:
            amho = temp

    amho_str_list = []
    for i in range(len(amho)):
        if amho[i:i+7] in mydict.values():
            amho_str = amho[i:i+56]
            amho_str_list.append(amho_str)
    
    try:
        for amho in amho_str_list:
            amho_list = []
            for j in range(8):
                J = j * 7
                alpha = ''
                for k in range(7):
                    alpha += amho[J + k]
                amho_list.append(alpha)
    except:
        pass

    print(amho_list)

    amho_num = []
    for i in range(8):
        for key, value in mydict.items():
            if amho_list[i] == value:
                amho_num.append(key)
                break
                
    print(amho_num)
    amho_TF = False
    cnt = 0
    for m in range(8):
        if m == 7:
            if (cnt + amho_num[7])%10 == 0:
                amho_TF = True
        elif m%2:
            cnt += amho_num[m]
        else:
            cnt += 3*(amho_num[m])

    # result = sum(amho_num)
    # #print(result)
    # #print("#%d %s" %(tc,amho))