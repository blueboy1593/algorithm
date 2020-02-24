import sys
sys.stdin=open("input.txt", "r")

# def palindrome(alist):
#     if alist == alist[::-1]:
#         return True
#     else:
#         return False
def palindrome(a):
    result = True
    for i in range(len(a) // 2):
        if a[i] != a[-i-1]:
            result = False
            break
    return result


for tc in range(1, 11):
    N = int(input())
    total_list=[]
    max_cnt=0
    Total_list_02 = []
    n = 100

    for i in range(100):
        # 좌우 행의 값을 추가하고 토탈 리스트 만들기
        xlist=list(input())
        total_list.append(xlist)
        # 몇개짜리로 리스트를 이룰지 결정.
    
    for i in range(100):
        for j in range(100,0,-1):
            # j개짜리를 순차적으로 만드는 코드
            for k in range(100-j+1):
                temp_list=[]
                for l in range(j):
                    temp_list.append(total_list[i][l+k])
                if palindrome(temp_list)==True:
                    if j > max_cnt:
                        max_cnt=j
                    break
                    
            if palindrome(temp_list)==True:
                break
        
    for i in range(n):
        Total_list_02.append([])
        
    for i in range(n):
        for j in range(n):
            Total_list_02[i].append(total_list[j][i])

    for i in range(100):
        for j in range(100,0,-1):   
            for k in range(100-j+1):
                temp_list=[]
                for l in range(j):
                    temp_list.append(Total_list_02[i][l+k])
                if palindrome(temp_list)==True:
                    if j > max_cnt:
                        max_cnt=j
                        break
                            
            if palindrome(temp_list)==True:
                break

    print("#%d %d" %(tc,max_cnt))
