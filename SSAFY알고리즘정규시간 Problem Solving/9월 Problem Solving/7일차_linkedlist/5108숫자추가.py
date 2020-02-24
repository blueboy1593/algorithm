import sys
sys.stdin = open("5108_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    num_list = list(map(int, input().split()))
    push = []
    for _ in range(M):
        a, b = map(int,input().split())
        push.append(a)
        push.append(b)

    for i in range(len(push)):
        if i%2 == 0:
            num_list.insert(push[i], push[i+1])
        else:
            pass

    result = num_list[L]

    print("#{} {}".format(tc, result))
    
    # 다들 insert를 쓰니깐 맞을 수밖에 없는 문제구만.