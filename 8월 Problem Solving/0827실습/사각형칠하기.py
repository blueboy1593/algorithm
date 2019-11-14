import sys
sys.stdin=open("im_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    bin_list=[ [0]*M for _ in range(N) ]
    map_list=[]
    my_dict = {}
    max_value = 0

    for d in range(11):
        my_dict[d]=0

    for i in range(K):
        temp=list(map(int,input().split()))
        map_list.append(temp)

    for k in range(K):
        color_on=True
        a = map_list[k][0]
        b = map_list[k][1]
        c = map_list[k][2]
        d = map_list[k][3]
        e = map_list[k][4]
        for i in range(a, c+1):
            for j in range(b, d+1):
                if e < bin_list[i][j]:
                    color_on=False
        if color_on== True:
            for i in range(a, c + 1):
                for j in range(b, d + 1):
                    bin_list[i][j]=e

    for i in range(N):
        for j in range(M):
            my_dict[bin_list[i][j]] += 1

    for value in my_dict.values():
        if value > max_value:
            max_value = value

    #print(bin_list)
    print("#%d %d" %(tc,max_value))
