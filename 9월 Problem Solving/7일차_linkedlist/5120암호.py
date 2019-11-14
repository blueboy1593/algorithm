import sys
sys.stdin = open("5120_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    N_list = list(map(int, input().split()))
    # ying = (N-1)//M
    # for i in range(N + ying):
    c = M
    for i in range(K):
        if c < len(N_list):
            added = N_list[c - 1] + N_list[c]
            N_list.insert(c, added)
        elif c == len(N_list):
            added = N_list[-1] + N_list[0]
            N_list.append(added)
        else:
            c = c - len(N_list)
            added = added = N_list[c - 1] + N_list[c]
            N_list.insert(c, added)
        c += M

    result = []
    if len(N_list) < 10:
        for _ in range (len(N_list)):
            result.append(N_list.pop())
    else:
        for _ in range (10):
            result.append(N_list.pop())
    
    result = ' '.join(map(str, result))
    print("#{} {}" .format(tc, result))