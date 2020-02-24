import sys
sys.stdin = open("키순서_input.txt", "r")

def compare_height(student):
    # 가는것부터
    queue = [student]
    while queue:
        stu = queue.pop(0)
        for j in range(1, N + 1):
            if injub[stu][j] == 1 and TF[j] == 0:
                TF[j] = 1
                queue.append(j)

    queue2 = [student]
    while queue2:
        stu = queue2.pop(0)
        for i in range(1, N + 1):
            if injub[i][stu] == 1 and TF[i] != 2:
                TF[i] = 2
                queue2.append(i)

    for k in range(1, N + 1):
        if TF[k] == 0:
            return False
    return True

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    M = int(input())
    injub = [ [0] * (N + 1) for _ in range(N + 1) ]
    for _ in range(M):
        a, b = map(int, input().split())
        injub[a][b] = 1
    # Check_TF = [True] * (N + 1)
    result = 0

    for student in range(1, N + 1):
        TF = [0] * (N + 1)
        TF[0] = 1
        TF[student] = 1
        if compare_height(student):
            result += 1
    
    print("#%d %d" %(tc, result))