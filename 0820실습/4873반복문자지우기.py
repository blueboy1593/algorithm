import sys
sys.stdin=open("sample_input.txt", "r")

T=int(input())

for tc in range(1,T+1):
    mun_list = list(input())
    while True:
        done = False
        for i in range(len(mun_list)-1):
            if mun_list[i] == mun_list[i+1]:
                mun_list.pop(i)
                mun_list.pop(i)
                done = True
                break
        if done == False:
            break
    print("#%d %d" %(tc,len(mun_list)))


