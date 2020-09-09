import sys
sys.stdin = open("input.txt", "r")

from heapq import heappop, heappush

N, M = map(int,input().split())
probs_arr = [ [] for _ in range(N + 1) ]
weights = [0] * (N + 1)
answer = []

for _ in range(M):
    a, b = map(int, input().split())
    probs_arr[a].append(b)
    weights[b] += 1

dequeue = []
for i in range(1, N + 1):
    if weights[i] == 0:
        heappush(dequeue, i)

while dequeue:
    c = heappop(dequeue)
    answer.append(c)
    if probs_arr[c] != []:
        for d in probs_arr[c]:
            weights[d] -= 1
            if weights[d] == 0:
                heappush(dequeue, d)

answer = ' '.join(map(str, answer))
print(answer)