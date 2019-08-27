import sys
sys.stdin=open("1220_input.txt", "r")

# def changexy(x):
#     l = len(x)
#     for i in range(l):
#         for j in range(l):
#             x[i][j], x[j][i] = x[j][i], x[i][j]
#     return x

T = 10
for tc in range(1, T+1):
    N = int(input())
    total_list=[]
    total_cnt = 0
    for i in range(N):
        temp = list(map(int, input().split()))
        total_list.append(temp)

    for i in range(100):
        stack = []
        cnt = 0
        for j in range(100):
            if total_list[j][i] != 0:
                stack.append(total_list[j][i])
        for k in range(len(stack)-1):
            if stack[k] != stack[k+1]:
                cnt += 1
        if stack[0]==2:
            cnt-=1
        if stack[-1]==1:
            cnt-=1
        total_cnt += cnt
    result = int(total_cnt/2) + 50
    print("#%d %d" %(tc, result))
