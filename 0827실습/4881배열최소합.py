import sys
sys.stdin=open("4881_input.txt", "r")

def getmaxhab(ca, TF, n):
    global N
    global hab_list
    if n==1:
        for k in range(N):
            if TF[k]==False:
                hab += ca[N-n][k]
                #print(hab)
                hab_list.append(hab)
    elif n == N:
        for i in range(n):
            hab = 0

            TF = [False] * N
            TF[i]=True
            hab += ca[N-n][i]

            getmaxhab(ca, n-1)
    else:
        for j in range(N):
            if TF[j]==False:
                TF[j]=True
                hab += ca[N-n][j]
                getmaxhab(ca, n-1)

T=int(input())
for tc in range(1, T+1):
    N = int(input())
    bingo=[]
    hab_list=[]
    for i in range(N):
        temp = list(map(int, input().split()))
        bingo.append(temp)

    getmaxhab(bingo, N)
    print(bingo)
    print(hab_list)