import sys
sys.stdin = open("7465_input.txt", "r")
from pprint import pprint

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    stack = []
    for _ in range(M):
        temp = list(map(int, input().split()))
        stack.append(temp)
    
    friend_list = [0] * (N + 1)
    friend_list[0] = 1
    cnt = 1
    if stack != []:
        a = stack.pop(0)
        friend_list[a[0]] = cnt
        friend_list[a[1]] = cnt
        
    while stack != []:
        flag = 0
        for i in range(len(stack)):
            a = stack[i]
            if friend_list[a[0]] == cnt:
                friend_list[a[1]] = cnt
                stack.pop(i)
                flag = 1
                break
            if friend_list[a[1]] == cnt:
                friend_list[a[0]] = cnt
                stack.pop(i)
                flag = 1
                break
        if flag == 0:
            cnt += 1
            b = stack.pop(0)
            friend_list[b[0]] = cnt
            friend_list[b[1]] = cnt
    
    for i in range(N + 1):
        if friend_list[i] == 0:
            cnt += 1
            friend_list[i] = cnt

    result = max(friend_list)

    if M == 0:
        result = N

    print("#%d %d" %(tc, result))