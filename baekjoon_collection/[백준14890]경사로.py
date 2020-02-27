N, L = map(int, input().split())
slope_way = []
for _ in range(N):
    slope_way.append(list(map(int, input().split())))
# 이 문제는 진짜 생각 싸움이라고 볼 수 있어.
# 단계가 무의미한...

# d 는 4방향 좌 우 상 하
# D = [(0, -1), (0, 1), (-1, 0), (1, 0)]
# d 는 -1과 +1로만 구성해도 되겠네!
def check_slope(L, j, d):
    slope_value = slope[j]
    for l in range(L):
        jj = j + d*l
        if not 0 <= jj < N:
            return False
        if visited[jj] == False and slope[jj] == slope_value:
            visited[jj] = True
        else:
            return False
    return True

result = 0
for i in range(N):
    slope = slope_way[i]
    flag = True
    visited = [ False ] * N
    for j in range(N - 1):
        if abs(slope[j] - slope[j + 1]) > 1: # 2 이상 차이가 나면 무적권
            flag = False
            break
        # 오른쪽이 1이 큰 경우와
        if slope[j] < slope[j + 1]: 
            TF = check_slope(L, j, -1)
            if TF == False:
                flag = False
                break
        # 왼쪽이 1이 큰 2가지 경우
        elif slope[j] > slope[j + 1]:
            TF = check_slope(L, j + 1, 1)
            if TF == False:
                flag = False
                break
    if flag == True:
        # print(slope)
        result += 1

for j in range(N):
    # 이 3줄의 코드를 쉽게 표현하는 방법을 찾으면 좋을 듯.
    slope = [0] * N
    for i in range(N):
        slope[i] = slope_way[i][j]
    flag = True
    visited = [ False ] * N
    for j in range(N - 1):
        if abs(slope[j] - slope[j + 1]) > 1: # 2 이상 차이가 나면 무적권
            flag = False
            break
        # 오른쪽이 1이 큰 경우와
        if slope[j] < slope[j + 1]: 
            TF = check_slope(L, j, -1)
            if TF == False:
                flag = False
                break
        # 왼쪽이 1이 큰 2가지 경우
        elif slope[j] > slope[j + 1]:
            TF = check_slope(L, j + 1, 1)
            if TF == False:
                flag = False
                break
    if flag == True:
        # print(slope)
        result += 1
# 45분. 쉬엄쉬엄
print(result)