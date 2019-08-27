
T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    aa_list = []
    for i in range(N):
        temp = list(map(int, input().split()))
        aa_list.append(temp)
    
    hab_list = []

    for j in range(N-K+1):
        for k in range(M-K+1):
            hab = 0
            for l in range(K):
                for m in range(K):
                    if l == 0 or l == K-1 or m == 0 or m == K-1:
                        hab += aa_list[l+j][m+k]

            hab_list.append(hab)
    max_hab = max(hab_list)
    print("#%d %d" %(tc, max_hab))