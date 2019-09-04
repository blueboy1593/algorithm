import sys
sys.stdin = open("1949_input.txt", "r")

# 맵 복사 후 깎는 함수 만들기
def copy_reduce():
    global N, K, max_bong
    for i in range(N):
        for j in range(N):
            for k in range(1, K + 1):
                # 맵 복사 과정
                copy_mount = [0] * N
                for m in range(N):
                    copy_mount[m] = mount[m][:]
                # 복사 후 k 깎기
                copy_mount[i][j] -= k
                
                # 봉우리 리스트에서 봉우리 정보를 가져와 깎이지 않았다면 탐색 시작.
                for bong in bong_list:
                    if bong != [i,j]:
                        y = bong[0]
                        x = bong[1]
                        cnt = 0
                        pre_height = max_bong
                        find_route(y, x, cnt, pre_height, copy_mount)
                        

# 봉우리에서 재귀 혹은 탐색으로 길찾기 함수
# 재귀를 사용하기때문에 카운트, 전값, 카피한 리스트값 모두 데려오기
def find_route(y, x, cnt, pre_height, copy_mount):
    global result, N
    height_save = pre_height
    # if copy_mount[2][3] == 8:
        # print(copy_mount, y, x, cnt, pre_height)
    cnt += 1
    for i in range(4):
        pre_height = height_save
        idy = y + dy[i]
        idx = x + dx[i]
        if 0 <= idy < N and 0 <= idx < N:
            a = copy_mount[idy][idx]
            if a < pre_height:
                pre_height = a
                find_route(idy, idx, cnt, pre_height, copy_mount)
            else:
                if cnt > result:
                    result = cnt
                

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    mount = []
    for _ in range(N):
        temp = list(map(int, input().split()))
        mount.append(temp)
    max_bong = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    result = 0

    # 맵에서 봉우리 찾기 (2개 이상이어야 함.)
    for i in range(N):
        for j in range(N):
            if mount[i][j] > max_bong:
                max_bong = mount[i][j]
    
    # 봉우리 좌표 리스트에 목록 넣기
    bong_list = []
    for i in range(N):
        for j in range(N):
            if mount[i][j] == max_bong:
                bong_list.append([i, j])
    
    copy_reduce()
    print("#%d %d" %(tc, result))