from heapq import heappop, heappush, heapify

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while len(scoville) > 1:
        a = heappop(scoville)
        if a >= K:
            return answer
        b = heappop(scoville)
        heappush(scoville, a + b*2)
        answer += 1
    if scoville[0] >= K:
        return answer
    else:
        return -1