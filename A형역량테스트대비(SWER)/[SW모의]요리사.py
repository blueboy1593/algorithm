import sys
sys.stdin = open("요리사_input.txt", "r")


# list로 변수명 안주지만 한번 해봐야지
def add_comb(list, index ,cnt):
    if cnt == comb_leng:
        comb_list.append(list[:])
        return
    cnt += 1
    for i in range(index + 1, N):
        list.append(i)
        add_comb(list, i, cnt)
        list.pop()

def count_synergy(comb):
    synergy = 0
    for i in range(comb_leng):
        iii = comb[i]
        for j in range(i + 1, comb_leng):
            jjj = comb[j]
            synergy += chef_synergy[iii][jjj]
            synergy += chef_synergy[jjj][iii]
    return synergy

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    chef_synergy = []
    for _ in range(N):
        chef_synergy.append(list(map(int, input().split())))
    min_chai = 99999999

    # 1을 포함해 만드는 조합으로 해보자.
    comb_list = []
    comb_leng = N//2
    initial_comb = [0]
    visited = [False] * N
    visited[0] = True
    add_comb(initial_comb, 0,1)

    # 반으로 나누는데 성공했으니 두개로 나누어 계산.
    for comb in comb_list:
        visited = [False] * N
        comb2 = []
        for co in comb:
            visited[co] = True
        for i in range(N):
            if visited[i] == False:
                comb2.append(i)

        result1 = count_synergy(comb)
        result2 = count_synergy(comb2)
        chai = abs(result1 - result2)
        min_chai = min(chai, min_chai)

    print('#%d %d' %(tc, min_chai))