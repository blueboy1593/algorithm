def solution(n):
    answer = 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    p1 = 1
    p2 = 2
    for _ in range(n - 3):
        p1, p2 = p2, p1 + p2
    
    answer = (p1 + p2)%1000000007
    return answer