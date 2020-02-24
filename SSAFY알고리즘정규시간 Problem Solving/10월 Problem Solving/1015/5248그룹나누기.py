import sys
sys.stdin = open("5248_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    wish_list = list(map(int, input().split()))
    visited = [0] * (N + 1)
    group_list = [[wish_list[0], wish_list[1]]]
    visited[wish_list[0]] = 1
    visited[wish_list[1]] = 1
    for i in range(2, len(wish_list)):
        if not i % 2:
            a = wish_list[i]
            b = wish_list[i + 1]
            flag = False
            for j in range(len(group_list)):
                if a in group_list[j]:
                    group_list[j].append(b)
                    visited[b] = 1
                    flag = True
                    break
                if b in group_list[j]:
                    group_list[j].append(a)
                    visited[a] = 1
                    flag = True
                    break
            if flag == False:
                group_list.append([a, b])
                visited[a] = 1
                visited[b] = 1

    solo = visited.count(0) - 1
    couple = len(group_list)
    result = solo + couple


    print("#%d %d" %(tc, result))
