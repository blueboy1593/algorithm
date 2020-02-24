import sys
sys.stdin = open("1258_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        temp = list(map(int, input().split()))
        arr.append(temp)
    visited = [ [False] * N for _ in range(N) ]
    rectangle = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0 and visited[i][j] == False:
                k = j
                l = i
                while True:

                    if k == N - 1 and arr[k][j] != 0:
                        garo = k - j + 1
                        break
                    if arr[i][k] == 0:
                        garo = k - j
                        break
                
                    k += 1
                while True:
                    
                    if l == N - 1 and arr[i][l] != 0:
                        sero = l - i + 1
                        break
                    if arr[l][j] == 0:
                        sero = l - i
                        break
                    l += 1
                    
                rectangle.append([sero, garo])
                for m in range(i, i + sero):
                    for n in range(j, j + garo):
                        visited[m][n] = True
    
    length = len(rectangle)
    # 새로이 안 람다. key는 정렬 기준값을 말하는 듯.
    rectangle.sort(key=lambda x: x[0])
    rectangle.sort(key=lambda x: x[0] * x[1])

    result = ''
    for rec in rectangle:
        result += ' '.join(map(str, rec)) + ' '
    print("#%d %s %s" %(tc,length,result))