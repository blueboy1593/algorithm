def solution(s):
    answer = [0, 0]
    while True:
        answer[0] += 1
        num = s.count('1')
        answer[1] += s.count('0')
        s = bin(num)[2:]
        if s == '1':
            break
    return answer