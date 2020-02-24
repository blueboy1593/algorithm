import sys
sys.stdin=open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    card = input()
    card_list = list(card)
    cnt = 0
    a_list = []
    b_list = []
    S = 13
    D = 13
    H = 13
    C = 13
    ERROR = False
    
    for key in card_list:
        a_list.append(key)
        cnt += 1
        if cnt == 3:
            b_list.append(a_list)
            a_list = []
            cnt = 0
    
    b_list_temp = []
    for b in b_list:
        
        if b in b_list_temp:
            ERROR = True
            break
        
        else:
            if b[0] == 'S':
                S -= 1
            if b[0] == 'D':
                D -= 1
            if b[0] == 'H':
                H -= 1
            if b[0] == 'C':
                C -= 1
        b_list_temp.append(b)
    if ERROR == True:
        print('#%d ERROR' %tc)
    else:
        print('#%d %d %d %d %d' %(tc, S, D, H, C))
