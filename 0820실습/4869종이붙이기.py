import sys
sys.stdin=open("4869_input.txt", "r")

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    n = int(N/10)
    f1 = 1
    f2 = 0
    result = f1 + f2
    if n > 1:
        for i in range(n-1):
            f3 = f1
            f1 = f1 + f2
            f2 = f3*2
            result = f1 + f2

    print("#%d %d" %(tc,result))