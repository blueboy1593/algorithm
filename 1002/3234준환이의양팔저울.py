import sys
sys.stdin = open("3234_input.txt", "r")

def make_per(k):
    if k == r:
        print(t)
    else:
        for i in range(n):
            if visited[i]:
                continue
            visited[i] = 1
            t[k] = i 
            make_per(k + 1)
            visited[i] = 0




T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    mass = list(map(int, input().split()))

    left = 0
    right = 0

    for 