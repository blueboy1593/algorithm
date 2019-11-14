import sys
sys.stdin=open("4880_input.txt", "r")

def getWinCard(ca, x, y):
    if ca[x]==ca[y]+1:
        return x
    elif ca[x]==ca[y]+2:
        return y
    elif ca[y]==ca[x]+1:
        return y
    elif ca[y]==ca[x]+2:
        return x
    else:
        return x

def getWinner(ca, L, R):
    if R==L:
        return L
    elif R-L==1:
        return getWinCard(ca, L, R)
        # a = ca[L]
        # b = ca[R]
        # ab = getWinCard(a,b)
        # if ab==True:
        #     return a
        # else:
        #     return ab
    else:
        half = (L+R)//2
        left = getWinner(ca, L, half)
        right = getWinner(ca, half+1, R)
        return getWinCard(ca, left, right)
        # if win == True:
        #     return left
        # else:
        #     return win

T=int(input())
for tc in range(1, T+1):
    N = int(input())
    card = list(map(int, input().split()))
    result = getWinner(card, 0, N-1)+1
    print("#%d %d" %(tc,result))
