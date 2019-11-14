import sys
sys.stdin = open("3752_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    grade = list(map(int, input().split()))

    DP = [0] * (N*100 +1)
    DP[0] = 1
    length = len(DP)
    temp = []

    for score in grade:
        for i in range(length):
            if DP[i] == 1:
                if i not in temp:
                    temp.append(i)
        
        for a in temp:
            DP[a + score] = 1
    
    print("#%d %d" %(tc, sum(DP)))