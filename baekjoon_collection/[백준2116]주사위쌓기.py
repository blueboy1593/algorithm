N = int(input())
marble = []
for _ in range(N):
    marble.append(list(map(int, input().split())))
max_value = 0

def side_value(num, arr):
    if num == 0 or num == 5:
        return max(arr[1], arr[2], arr[3], arr[4])
    elif num == 1 or num == 3:
        return max(arr[0], arr[2], arr[5], arr[4])
    elif num == 2 or num == 4:
        return max(arr[0], arr[1], arr[5], arr[3])

def select_num(k, arr):
    if k == 0:
        return arr[5]
    elif k == 1:
        return arr[3]
    elif k == 2:
        return arr[4]
    elif k == 3:
        return arr[1]
    elif k == 4:
        return arr[2]
    elif k == 5:
        return arr[0]

# 0, 6 / 1, 3 / 2, 4 는 세트
for i in range(6):
    arr = marble[0]
    num = arr[i]
    temp_value = side_value(i, arr)
    for j in range(1, N):
        arr = marble[j]
        for k in range(6):
            if num == arr[k]:
                num = select_num(k, arr)
                break
        temp_value += side_value(k, arr)
    max_value = max(max_value, temp_value)

print(max_value)

# 백준 남의 코드 중 상당히 괜찮은 코드!
# back = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
# N = int(input())
# data = [list(map(int, input().split())) for _ in range(N)]
# ans = 0
# for i in range(6):
#     n = 0
#     for j in range(N):
#         data[j][i] -= 100
#         data[j][back[i]] -= 100
#         n += max(data[j])
#         data[j][i] += 100
#         data[j][back[i]] += 100
#         if j == N - 1:
#             continue
#         i = data[j + 1].index(data[j][back[i]])
#     if n > ans:
#         ans = n
# print(ans)