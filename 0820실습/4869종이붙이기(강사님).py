import sys
sys.stdin=open("4869_input.txt", "r")

def paper(w):
    if w == n:
        return 1
    if w > n:
        return 0
    return paper(w+10) + paper(w+20)*2

TC = int(input())
for tc in range(1, TC+1):
    n = int(input())
    r = paper(0)
    print("#%d %d" %(n, r))