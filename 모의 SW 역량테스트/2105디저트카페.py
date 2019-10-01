import sys
sys.stdin = open("2105_input.txt", "r")
from pprint import pprint
dx = [1, -1, -1, 1]
dy = [1, 1, -1, -1]







T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    dessert = [ [list(map(int, input().split()))] for _ in range(N) ]
    pprint(dessert)
    for i in range(1, N - 1):
        for j in range(0, N - 2):
            find_diamond(i, j)