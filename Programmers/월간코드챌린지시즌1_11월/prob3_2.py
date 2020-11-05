from collections import Counter

def solution(a):
    if len(a) <= 1:
        return 0

    counters = Counter(a)
    star = counters.most_common()[0][0]
    if a[0] == star:
        button = True
    else:
        button = False
    answer = 1
    for i in range(1, len(a)):
        if answer % 2 == 0:
            if a[i] == star:
                button = True
                answer += 1
            else:
                button = False
                answer += 1
            continue

        if button == True and a[i] != star:
            button = False
            answer += 1
        elif button == False and a[i] == star:
            button = True
            answer += 1

    if answer % 2:
        answer -= 1
    return answer


solution([0])
solution([5,2,3,3,5,3])
solution([0,3,3,0,7,2,0,2,2,0])