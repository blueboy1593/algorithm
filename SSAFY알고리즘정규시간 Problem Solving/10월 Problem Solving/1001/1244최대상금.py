import sys
sys.stdin = open("1244_input.txt", "r")

# dictionary, list 등등 dp를 하기에 가장 좋은건 뭘까?

def change_two(num, i, j):
    num = list(str(num))
    if len(num) < n:
        num.insert(0, '0')
    num[i], num[j] = num[j], num[i]
    new_num = int(''.join(num))
    DP_list[new_num] = 1
    return

T = int(input())
for tc in range(1, T + 1):
    number, change = input().split()
    n = len(number)
    # flag0 = False
    # for char in number:
    #     if char == '0':
    #         flag0 = True
    DP_list = [0] * (10 ** len(number))
    DP_list[int(number)] = 1
    change = int(change)
    for _ in range(change):
        DP_list2 = DP_list[:]
        DP_list = [0] * (10 ** len(number))
        for k in range(10 ** n):
            if DP_list2[k] == 1:
                for i in range(n):
                    for j in range(i + 1, n):
                        change_two(k, i, j)
    
    for i in range(10 ** n - 1, 0, -1):
        if DP_list[i] == 1:
            result = i
            break
    
    print("#%d %d" %(tc, result))