def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    dis_list = [rocks[0] - 0]
    for i in range(len(rocks) - 1):
        dis_list.append(rocks[i + 1] - rocks[i])
    dis_list.append(distance - rocks[-1])
    print(dis_list)
    for _ in range(n):
        minimum = (float('inf'), 1, 0)
        for i in range(len(dis_list) - 1):
            small = min(dis_list[i], dis_list[i + 1])
            big = max(dis_list[i], dis_list[i + 1])
            if small < minimum[0]:
                minimum = (small, big, i)
            elif small == minimum[0]:
                if small + big < minimum[0] + minimum[1]:
                    minimum = (small, big, i)
        dis_list.pop(minimum[2])
        dis_list.pop(minimum[2])
        dis_list.insert(i, minimum[0] + minimum[1])
    answer = min(dis_list)
    return answer

solution(25, [2, 14, 11, 21, 17], 2)