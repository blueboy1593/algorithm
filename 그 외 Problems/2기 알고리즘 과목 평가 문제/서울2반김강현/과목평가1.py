
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())    
    count = 0
    total_list = []
    for i in range(N):
        temp=[]
        for j in range(N):
            temp.append(0)    
        total_list.append(temp)
    
    for xy in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                total_list[x][y] = 1
    
    for i in range(N):
        for j in range(N):
            if total_list[i][j] == 1:
                count += 1
    
    print("#%d %d" %(tc,count))