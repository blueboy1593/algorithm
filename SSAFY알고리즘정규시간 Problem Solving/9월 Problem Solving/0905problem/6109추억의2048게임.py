from pprint import pprint
import sys
sys.stdin = open("6109_input.txt", "r")

def left_go():
    for i in range(N):
        stack = []
        for j in range(N):
            a = tyle[i][j]
            if a != 0:
                if stack == []:
                    stack.append(a)
                    term = False
                else:
                    if stack[-1] == a and term == False:
                        stack[-1] = a + a
                        term = True
                    else:
                        stack.append(a)
                        term = False
        for k in range(len(stack)):
            new_tyle[i][k] = stack[k]

def change(arr):
    for i in range(len(arr)):
        arr[i].reverse()
    return arr

T = int(input())
for tc in range(1, T + 1):
    N, S = input().split()
    N = int(N)
    tyle = []
    new_tyle = [[0]*N for _ in range(N)]

    for _ in range(N):
        temp = list(map(int, input().split()))
        tyle.append(temp)

    if S == 'left':
        left_go()
    if S == 'up':
        tyle = list(zip(*tyle))
        left_go()
        new_tyle = list(map(list, zip(*new_tyle)))
    if S == 'right':
        change(tyle)
        left_go()
        change(new_tyle)
    if S == 'down':
        tyle = list(map(list, zip(*tyle)))
        change(tyle)
        left_go()
        change(new_tyle)
        new_tyle = list(map(list, zip(*new_tyle)))
    
    print("#%d" %tc)
    for i in range(N):
        temp = ' '.join(map(str,new_tyle[i]))
        print(temp)