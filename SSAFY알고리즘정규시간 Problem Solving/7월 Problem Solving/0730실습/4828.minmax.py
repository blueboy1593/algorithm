N = int(input())

for i in range(1, N + 1):
    pos = int(input()) # 양수의 개수
    pos_list = list(map(int, input().split()))
    pmax = 0
    pmin = pos_list[0]
    for num in pos_list:
        if num > pmax:
            pmax = num
        if num < pmin:
            pmin = num
    chai = pmax - pmin
    print('#%d %d' %(i,chai))
            