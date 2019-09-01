import sys
sys.stdin = open("5122_input.txt", "r")

T = int(input())

def doC(change):
    base_list[change[1]] = change[2]
    return

def doD(change):
    base_list.pop(change[1])

def doI(change):
    base_list.insert(change[1], change[2])

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    base_list = list(map(int, input().split()))
    change_list = []
    for _ in range(M):
        temp = list(input().split())
        for i in range(len(temp)):
            if temp[i].isdigit():
                temp[i] = int(temp[i])
        change_list.append(temp)
    
    try:
        for i in range(len(change_list)):
            if change_list[i][0] == 'C':
                doC(change_list[i])
            elif change_list[i][0] == 'D':
                doD(change_list[i])
            elif change_list[i][0] == 'I':
                doI(change_list[i])
            result = base_list[L]
    except IndexError:
        result = -1

    print("#%d %d" %(tc, result))