import sys
sys.stdin = open("1961_input.txt")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = []
    for _ in range(N):
        temp = list(map(str, input().split()))
        matrix.append(temp)

    string90 = []
    for j in range(N):
        st90 = ''
        for i in range(N - 1, -1, -1):
            st90 += matrix[i][j]
        string90.append(st90)

    string180 = []
    for i in range(N - 1, -1, -1):
        st180 = ''
        for j in range(N -1, -1, -1):
            st180 += matrix[i][j]
        string180.append(st180)

    string270 = []
    for j in range(N - 1, -1, -1):
        st270 = ''
        for i in range(N):
            st270 += matrix[i][j]
        string270.append(st270)

    print("#%d" %tc)
    for t in range(N):
        print(string90[t], string180[t], string270[t])
