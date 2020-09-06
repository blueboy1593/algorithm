from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    # people.reverse()
    people = deque(people)
    while people:
        answer += 1
        heaviest = people.pop()
        if people:
            if people[0] + heaviest <= limit:
                people.popleft()

        
    return answer

solution([70, 50, 80, 50], 100)