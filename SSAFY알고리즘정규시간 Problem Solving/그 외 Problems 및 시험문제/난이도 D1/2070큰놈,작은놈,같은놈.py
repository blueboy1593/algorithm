import sys
sys.stdin=open("input.txt", "r")

T = int(input())

def compare(x, y):
    if x < y:
        return '<'
    elif x == y:
        return '='
    elif x > y:
        return '>'

for tc in range(1, T+1):
    x, y = map(int, input().split())
    
    print('#%d %s' %(tc, compare(x,y)))