import sys
sys.stdin=open("sample_input.txt", "r")

T=int(input())

for tc in range(1, T+1):
    first=input()
    second=input()
    a = 0
    if first in second:
        a=1
    
    print("#%d %d" %(tc, a))