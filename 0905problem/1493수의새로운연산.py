import sys
sys.stdin = open("1493_input.txt", "r")

def find_sum(num):
    summ = num * (num + 1)//2
    return summ

def find_coordinate(num):
    for i in range(200):
        if find_sum(i) == num:
            x = i
            y = 1
            return (x, y)
        elif find_sum(i) > num:
            a = find_sum(i - 1)
            b = i + 1
            c = num - a
            x = c
            y = b - x
            return (x, y)

def find_value(x, y):
    n = x + y -2
    base = find_sum(n)
    value = base + x
    return value

T = int(input())
for tc in range(1, T + 1):
    p, q = map(int, input().split())
    aa = find_coordinate(p)
    bb = find_coordinate(q)
    cc = (aa[0] + bb[0], aa[1] + bb[1])
    result = find_value(cc[0], cc[1])
    
    print("#%d %d" %(tc, result))