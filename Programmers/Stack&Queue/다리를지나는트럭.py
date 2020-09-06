def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_trucks = [] # 다리를 건너는 트럭
    trucks_time = [] # 트럭이 다리를 다 건너고 빠지는 시간대 기록
    time = 0
    while truck_weights:
        time += 1
        # 1번 트럭 내려줄 때가 되었으면, 내려주기
        if trucks_time != []:
            if trucks_time[0] == time:
                bridge_trucks.pop(0)
                answer = trucks_time.pop(0)

        # 2번 다리에 트럭 올리기
        # 만약 다리를 건너는 트럭들의 무게와 새로 들어올 트럭 무게의 합이 가능 범주라면
        if sum(bridge_trucks) + truck_weights[0] <= weight:
            temp = truck_weights.pop(0)
            bridge_trucks.append(temp)
            trucks_time.append(time + bridge_length)
    if trucks_time != []:
        answer = trucks_time[-1]
    return answer