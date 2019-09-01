import sys
sys.stdin = open("5102_input.txt", "r")

TC = int(input())

for test_case in range(1, TC+1):
    V, E = map(int, input().split())
    data = []
    for i in range(E):
        temp = list(map(int, input().split()))
        data.append(temp)


    start, end = map(int, input().split())

    dic = {}

    for E_start, E_end in data:
        if dic.get(E_start) :
            dic[E_start].append(E_end)
        if dic.get(E_end) :
            dic[E_end].append(E_start)
        if not dic.get(E_start):
            dic[E_start] = [E_end]
        if not dic.get(E_end):
            dic[E_end] = [E_start]
    #print(dic)

    stack = []
    count = 0
    visited = [False] * (V+1)
    visited[0] = True
    while True:

        count += 1
        visited[start] = True

        if start in dic.keys():
            for v in dic[start]:
                if visited[v] == False:
                    stack.append([v, count])
        print(stack)
        if stack != []:
            start, count = stack.pop(0)
        # print(start, count)
        if start == end:
            break

    

    print("#{} {}".format(test_case, count))