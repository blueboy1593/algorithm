def solution(people, limit):
    answer = 0
    people.sort()
    while people:
        answer += 1
        lightest = people.pop(0)
        for i in range(len(people) - 1, -1, -1):
            if lightest + people[i] <= limit:
                people.pop(i)
                break

    return answer