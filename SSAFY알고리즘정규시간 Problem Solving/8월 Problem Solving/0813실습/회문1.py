import sys
sys.stdin=open("input.txt", "r")

def palindrome(alist):
    if alist == alist[::-1]:
        return True
    else:
        return False

for tc in range(1, 11):
    N = int(input())
    total_list=[]
    total_count=0
    for i in range(8):
        # 좌우 행의 값을 추가하고 토탈 리스트 만들기
        xlist=list(input())
        total_list.append(xlist)
        for j in range(8-N+1):
            temp_list=[]
            for k in range(N):
                temp_list.append(xlist[j+k])
            if palindrome(temp_list)==True:
                total_count += 1
    for l in range(8):
        for m in range(8-N+1):
            temp_list=[]
            for n in range(N):
                temp_list.append(total_list[m+n][l])
            if palindrome(temp_list)==True:
                total_count += 1
        
    print("#%d %d" %(tc,total_count))
