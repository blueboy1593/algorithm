import sys
sys.stdin = open("input.txt", "r")
# 이 코드는 input.txt파일에서 인풋을 가져오는 코드이다.

for tc in range(1, 11):
    N = int(input())
    heights = list(map(int, input().split()))

def getMax(idx):
    tmax = 

for i in range(2, N -2):
    side = getMax()
    if side < heights[i]:
        view += heights[i] - side

print('#%d %d' %(tc, view))