import sys
sys.stdin=open("sample_input.txt","r")

T = int(input())

def sort(list):
    l = len(list)
    for j in range(l):
        for i in range(l-1):
            if list[i]> list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
    return(list)

for tc in range(1, T+1):
    N = int(input())
    N_list = list(map(int, input().split()))
    SNL = sort(N_list) # sorted N list
    leng = len(SNL)
    result = []

    for k in range(5):
        result.append(SNL[leng-k-1])
        result.append(SNL[k])

    print("#"+str(tc)+' ', end='')
    print(' '.join(map(str, result)))