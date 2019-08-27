T = int(input())

for tc in range(1, T+1):
    N = int(input())
    total_list=[]
    count=0
    for i in range(N):
        temp = list(map(int, input().split()))
        total_list.append(temp)
    
    for i in range(N):
        for j in range(N):
            if total_list[i][j] > 0:
                total_list[i][j] = 0
                if i == 0 and j == 0:
                    if total_list[i+1][j]==0 and total_list[i+1][j+1]==0 and total_list[i][j+1]==0:
                        count += 1
                elif i == 0 and j == N-1:
                    if total_list[i+1][j]==0 and total_list[i+1][j-1]==0 and total_list[i][j-1]==0:
                        count += 1
                elif i == N-1 and j == 0:
                    if total_list[i-1][j]==0 and total_list[i-1][j+1]==0 and total_list[i][j+1]==0:
                        count += 1
                elif i == N-1 and j == N-1:
                    if total_list[i-1][j]==0 and total_list[i-1][j-1]==0 and total_list[i][j-1]==0:
                        count += 1
                elif i == 0:
                    if total_list[i+1][j]==0 and total_list[i+1][j-1]==0 and total_list[i+1][j+1]==0 and total_list[i][j+1]==0 and total_list[i][j-1]==0:
                        count += 1
                elif i == N-1:
                    if total_list[i-1][j]==0 and total_list[i-1][j-1]==0 and total_list[i-1][j+1]==0 and total_list[i][j+1]==0 and total_list[i][j-1]==0:
                        count += 1
                elif j == 0:
                    if total_list[i+1][j+1]==0 and total_list[i][j+1]==0 and total_list[i-1][j+1]==0 and total_list[i+1][j]==0 and total_list[i-1][j]==0:
                        count += 1
                elif j == N-1:
                    if total_list[i+1][j-1]==0 and total_list[i][j-1]==0 and total_list[i-1][j-1]==0 and total_list[i+1][j]==0 and total_list[i-1][j]==0:
                        count += 1
                else:
                    if total_list[i+1][j]==0 and total_list[i+1][j-1]==0 and total_list[i+1][j+1]==0 and total_list[i][j+1]==0 and total_list[i][j-1]==0 and total_list[i-1][j]==0 and total_list[i-1][j-1]==0 and total_list[i-1][j+1]==0:
                        count += 1
                        break
                    else:
                        pass

    print("#%d %d" %(tc,count))