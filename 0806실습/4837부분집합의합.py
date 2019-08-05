
# 부분집합 만드는 것은 다시 해봐야할 듯.
A = list(range(1,13))
subset_A = []
for i in range(1<<len(A)):
    temp_list = []
    for j in range(len(A)):
        if i & (1<<j):
            temp_list.append(A[j])
    subset_A.append(temp_list)

T = int(input())
# 부분 집합을 다 뽑는 것 말고는 방법이 쉽지 않겠지? for문으로 돌리기 어렵자나.
for num in range(1, T+1):
    N, K = map(int, input().split())
    count = 0
    for subset in subset_A:
        if len(subset) == N:
            if sum(subset) == K:
                count += 1

    print("#%d %d" %(num,count))