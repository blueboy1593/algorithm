import sys
sys.stdin=open("sample_input.txt", "r")

T=int(input())

for tc in range(1,T+1):
    V, E = map(int,input().split())
    go_list=[]
    for i in range(E):
        alist = list(map(int, input().split()))
        go_list.append(alist)
    S, G = map(int, input().split())
    # 여기까지가 입력 받기.

    dep_list = []
    for go in go_list:
        if S == go[0]:
            dep_list.append(go[1])
    for i in range(10):
        for dep in dep_list:
            for go in go_list:
                if dep == go[0] and go[1] not in dep_list:
                    dep_list.append(go[1])

    if G in dep_list:
        result = 1
    else:
        result = 0
    
    print("#%d %d" %(tc,result))
