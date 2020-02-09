from itertools import combinations
from pprint import pprint

N = int(input())
ingu = list(map(int, input().split()))
injub_list = [ [0] * N for _ in range(N) ]
for i in range(N):
    data = list(map(int, input().split()))
    for j in range(1, len(data)):
        p = data[j]
        injub_list[i][p - 1] = 1
        injub_list[p - 1][i] = 1
# pprint(injub_list)

# 조합을 다 구해봐?
# 1단계 가능한 모든 조합 경우의 수 구하기.
comb_list = []
half_N = N // 2
# 조합의 뼈대 만들기
base = []
for i in range(N):
    base.append(i)
for k in range(1, half_N + 1):
    temp = map(list,combinations(base, k))
    # temp = combinations(base, k)
    for a in temp:
        comb_list.append(a)
# print(comb_list)

# 2단계 각각 조합에 대해 visited 만들구 아 인접리스트부터
# 인접 리스트 만들기. 쉽게 만들었다.
# 노트에 적어둔 것대로 이제 순회공연.
def check_tree(num):
    stack = []
    for j in range(N):
        if injub_list[num][j] == 1 and visited[j] == False:
            stack.append(j)
            visited[j] = True
    while stack:
        sta = stack.pop()
        for j in range(N):
            if injub_list[sta][j] == 1 and visited[j] == False:
                stack.append(j)
                visited[j] = True

min_answer = 99999999
for comb in comb_list:
    # 이 방법 은근히 시간 오래 걸릴 것 같기도 하다
    visited = [False] * N
    visited2 = [False] * N
    num1 = comb[0]
    visited[num1] = True
    check_tree(num1)
    for k in range(N):
        if k in comb:
            if visited[k] == True:
                visited2[k] = True
    # 돌아가는 로직 뭐냐...

    visited = [False] * N
    for i in range(N):
        if i not in comb:
            num2 = i
            break
    visited[num2] = True
    check_tree(num2)
    for k in range(N):
        if k not in comb:
            if visited[k] == True:
                visited2[k] = True
    if visited2 == [True] * N:
        # 여기는 인구 비교 로직!!!
        sum1 = 0
        sum2 = 0
        for k in range(N):
            if k in comb:
                sum1 += ingu[k]
            else:
                sum2 += ingu[k]

        if abs(sum1 - sum2) < min_answer:
            min_answer = abs(sum1 - sum2)
    else:
        continue

if min_answer == 99999999:
    min_answer = -1
print(min_answer)