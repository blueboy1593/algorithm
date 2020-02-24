import sys
sys.stdin = open("3752_input.txt", "r")

T = int(input())

# 그거 해보자 list에 index로 점수 기입해보기.

def DFS(i, jumsoo):
    jumsoo += grade[i]
    grade_set.add(jumsoo)

    for j in range(i + 1, N):
        TF[j] = False
        DFS(j, jumsoo)
        TF[j] = True


for tc in range(1, T + 1):
    N = int(input())
    grade = list(map(int, input().split()))
    grade_set = set()
    
    for i in range(len(grade)):
        TF = [ False ] * N
        jumsoo = 0
        DFS(i, jumsoo)    
    
    result = len(grade_set) + 1

    print("#%d %d" %(tc, result))