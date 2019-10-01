import sys
sys.stdin = open("3752_input.txt", "r")

T = int(input())

def DFS(i, jumsoo):
    jumsoo += grade[i]
    grade_list[jumsoo] = 1

    for j in range(i + 1, N):
        if TF[j] == False:
            TF[j] = True
            DFS(j, jumsoo)
            TF[j] = False


for tc in range(1, T + 1):
    N = int(input())
    grade = list(map(int, input().split()))
    grade_list = [0] * (N*100 +1)
    
    for i in range(len(grade)):
        TF = [ False ] * N
        jumsoo = 0
        DFS(i, jumsoo)
    
    result = sum(grade_list) + 1

    print("#%d %d" %(tc, result))