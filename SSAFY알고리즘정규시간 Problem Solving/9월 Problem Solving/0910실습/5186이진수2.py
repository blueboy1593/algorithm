import sys
sys.stdin = open("5186_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = float(input())
    result = ''
    for i in range(12):
        divider = (1/2) ** (i + 1)
        if divider <= N:
            N -= divider
            result += '1'
        else:
            result += '0'
        if N == 0:
            break
    
    if N != 0:
        result = 'overflow'
    print("#%d %s" %(tc, result))