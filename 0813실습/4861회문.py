import sys
sys.stdin=open("sample_input.txt", "r")

T=int(input())

def palin(list):
    if list == list[::-1]:
        return list

for tc in range(1, T+1):
    N, M = map(int, input().split())
    total_list=[]
    for i in range(N):
        garo_list=list(input())
        total_list.append(garo_list)

    for alist in total_list:
        for l in range(N-M+1):
            blist=alist[l:l+M]
            p = palin(blist)
            if p != None:
                result = p
    
    for j in range(N):
        for k in range(N-M+1):
            test_list=[]
            for m in range(k, k+M):
                test_list.append(total_list[m][j])
            pp = palin(test_list)
            if pp != None:
                result = pp
    
    result = ''.join(result)

    print("#%d %s" %(tc,result))