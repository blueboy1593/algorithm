N, M, X = map(int, input().split())
party_time = [ [0] * (N + 1) for _ in range(N + 1) ]
for _ in range(M):
    s, e, t = map(int, input().split())
    party_time[s][e] = t

longest_student = 0

def find_short(a, b):
    distance_list = [99999999] * (N + 1)
    queue = [a]
    while queue:
        que = queue.pop(0)
        for j in range(1, N + 1):
            if party_time[que][j] != 0:


for num in range(1, N + 1):
    if num != X:
        find_short(num, X)
        find_short(X, num)