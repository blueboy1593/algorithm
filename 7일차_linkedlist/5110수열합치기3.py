import sys
sys.stdin = open("5110_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    suyeol = []
    push = False
    for _ in range(M):
        temp = list(map(int, input().split()))
        suyeol.append(temp)

    base_list = suyeol[0]
    for i in range(1, M):
        push = False
        for j in range(len(base_list)):
            if suyeol[i][0] < base_list[j]:
                base_list = base_list[:j] + suyeol[i] + base_list[j:]
                push = True
                break
        if push == False:
            base_list = base_list + suyeol[i]

    result = []
    len_base = len(base_list)
    if len_base < 10:
        for _ in range(len_base):
            result.append(base_list.pop())
    else:
        result = base_list[-10:]
        result.reverse()

    result = ' '.join(map(str, result))
    print("#{} {}".format(tc, result))