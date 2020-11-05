from collections import Counter

def solution(a):
    if len(a) <= 1:
        return 0
    answer = [0]
    N = len(a)
    
    def check_star(arr):
        cntt = Counter(arr)
        num = cntt.most_common()[0][0]
        for i in range(len(arr)):
            if i % 2 == 0:
                if arr[i] == arr[i + 1]:
                    return False
                if arr[i] == num or arr[i + 1] == num:
                    continue
                else:
                    return False
        return True
    
    def dfs(i, arr):
        if len(arr) > answer[0] and len(arr) % 2 == 0:
            if check_star(arr):
                answer[0] = len(arr)
        for j in range(i, N):
            dfs(j + 1, arr + [a[j]])
    dfs(0, [])
    return answer[0]