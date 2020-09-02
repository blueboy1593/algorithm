# Idea 문제
# 가로 길이를 세로 길이로 등분해서 정수가 나오면 패스, 소수가 나오면 위아래 사용불가로 체크
# 세로 길이를 가로 길이로 등분해서 정수가 나오면 패스, 소수가 나오면 좌우 사용불가로 체크

def solution(w,h):
    answer = 0
    paper = []
    for _ in range(h):
        paper.append([1] * w)
    
    # 가로 길이 분할
    for i in range(1, h + 1):
        x_point = w * (i / h)
        x_int_point = int(x_point)
        if x_int_point == x_point: # 정수 체크 되는지 확인
            pass
        else:
            paper[i][x_int_point] = 0
            paper[i - 1][x_int_point] = 0
    # 가로 길이만 해봐도 될 것 같기도 한데, 한번 돌려서 확인해보자

    for i in range(h):
        for j in range(w):
            if paper[i][j] == 1:
                answer += 1

    # print(*paper, sep='\n')
    return answer

solution(8, 12)