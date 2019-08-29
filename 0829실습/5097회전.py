import sys
sys.stdin = open("5097_input.txt", "r")

T = int(input())

def popsend(ex):
    ex.append(ex.pop(0))
    return ex

for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    for i in range(M):
        popsend(data)
    result = data[0]

    print("#%d %d" %(tc, result))