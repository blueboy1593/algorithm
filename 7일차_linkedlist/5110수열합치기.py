import sys
sys.stdin = open("5110_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
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
                base_list.insert(j , suyeol[i])
                push = True
                # print(base_list)
                for k in range(N):
                    base_list.insert(j , suyeol[i].pop())
                base_list.remove([])
                # print(base_list)
                break
        if push == False:
            base_list = base_list + suyeol[i]
    
    result = []
    if len(base_list) < 10:
        for _ in range (len(base_list)):
            result.append(base_list.pop())
    else:
        for _ in range (10):
            result.append(base_list.pop())

    result = ' '.join(map(str,result))
    print("#{} {}" .format(tc, result))
    