n = int(input())

for test in range(1, n+1):
    N,M = map(int,input().split())
    ai_list = list(map(int, input().split()))
    ai_sum_list = []
    for i in range(len(ai_list)-M+1):
        ai_sum = 0
        for j in range(M):
            ai_sum += ai_list[i + j]
        ai_sum_list.append(ai_sum)
    aimax = max(ai_sum_list)
    aimin = min(ai_sum_list)
    result = aimax-aimin
    print('#%d %d'%(test,result))
