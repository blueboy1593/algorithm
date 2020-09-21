from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)

    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        cnt = 0
        while progresses:
            if progresses[0] < 100:
                break
            else:
                cnt += 1
                progresses.popleft()
                speeds.popleft()
        if cnt > 0:
            answer.append(cnt)
    return answer