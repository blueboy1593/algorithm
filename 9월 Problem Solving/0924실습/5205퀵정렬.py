import sys
sys.stdin = open("5204_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    jungsu = list(map(int, input().split()))
    L = N//2

    jungsu.sort()
    a = jungsu[L]
    print("#%d %d" %(tc, a))