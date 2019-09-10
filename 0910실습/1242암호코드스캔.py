import sys
sys.stdin = open("1242_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    mydict = {}
    N, M = map(int, input().split())
    bikyo = '0'*M
    for _ in range(N):
        temp = input()
        # 암호가 들어있는 배열이 나왔을때
        if temp != bikyo:
            cnt = 0
            amho = ''
            flag = False
            for i in range(len(temp)):
                if temp[i] != '0':
                    flag = True
                if flag == True:
                    cnt += 1
                    amho += temp[i]
                if cnt % 14 == 0 and flag == True:
                    if i == M - 1:
                        if amho not in mydict.keys():
                            mydict[amho] = 1
                        else:
                            mydict[amho] += 1
                        amho = ''
                        flag = False
                        cnt = 0
                    elif temp[i+1] == '0':
                        if amho not in mydict.keys():
                            mydict[amho] = 1
                        else:
                            mydict[amho] += 1
                        amho = ''
                        flag = False
                        cnt = 0
                    else:
                        pass
                    
    print(mydict)


