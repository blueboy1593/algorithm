import sys
sys.stdin = open("5110_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    push = False
    base_list = list(map(int, input().split()))

    for k in range(1, M):
        temp = list(map(int, input().split()))
        push = False

        for j in range(len(base_list)):
            if temp[0] < base_list[j]:
                base_list[j:0] = temp
                push = True
                break
        if push == False:
            base_list = base_list + temp

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