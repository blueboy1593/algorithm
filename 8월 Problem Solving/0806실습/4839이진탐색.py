
T = int(input())

def izin(P, page):
    l = 1
    r = P
    cnt = 0
    c = 0
    while c != page:
        c = int((l + r)/2)
        if c == page:
            return cnt
        elif page < c:
            r = c
            cnt += 1
        else:
            l = c
            cnt += 1

for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    A_cnt = izin(P, A)
    B_cnt = izin(P, B)
    
    if A_cnt < B_cnt:
        print("#%d A" %tc)
    elif A_cnt == B_cnt:
        print("#%d 0" %tc)
    else:
        print("#%d B" %tc)
