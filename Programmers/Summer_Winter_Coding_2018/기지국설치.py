def solution(n, stations, w):
    answer = 0
    apart = [0] * n
    for sta in stations:
        sta -= 1
        try:
            for i in range(-w, w + 1):
                sta_n = sta + i
                apart[sta_n] = 1
        except IndexError as identifier:
            pass

    cnt = 0
    for i in range(n):
        if apart[i] == 1:
            if cnt > 0:
                answer += ((cnt - 1) // (w*2 + 1)) + 1
                cnt = 0
        else:
            cnt += 1
    if cnt > 0:
        answer += ((cnt - 1) // (w*2 + 1)) + 1

    return answer

# solution(11, [4, 11], 1)
solution(16,[9], 2)