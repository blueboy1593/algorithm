def solution(n):
    answer = []
    pyramid = [ [0] * i for i in range(1, n + 1) ]
    i, j = 0, 0
    n_n = 1
    D = [(1,0), (0,1), (-1,-1)]
    d = 0

    while True:
        pyramid[i][j] = n_n
        idy = i + D[d][0]
        jdx = j + D[d][1]
        if d == 0:
            if idy < n:
                if pyramid[idy][jdx] == 0:
                    pyramid[idy][jdx] = n_n
                    i = idy
                    j = jdx
                    n_n += 1
                    continue
            d = 1
        elif d == 1:
            if jdx <= idy:
                if pyramid[idy][jdx] == 0:
                    pyramid[idy][jdx] = n_n
                    i = idy
                    j = jdx
                    n_n += 1
                    continue
            d = 2
        elif d == 2:
            if pyramid[idy][jdx] == 0:
                pyramid[idy][jdx] = n_n
                i = idy
                j = jdx
                n_n += 1
                continue
            d = 0
        if n_n == n*(n+1)/2:
            break
    
    for k in range(n):
        answer += pyramid[k]
    return answer

solution(5)