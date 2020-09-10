def solution(citations):
    citations.sort()
    for i in range(len(citations)//2, 0, -1):
        if citations[i - 1] != citations[i]:
            return citations[i]