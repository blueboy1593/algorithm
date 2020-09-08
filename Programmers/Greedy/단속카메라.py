# 좀 찜찜한 로직이지만, 해보자.
def solution(routes):
    answer = 0

    # 주어진 조건으로 고속도로 1씩 더하고, 계산 편하게 30000 더해주는 로직
    expressway = [0] * 60001
    for i in range(len(routes)):
        routes[i] = [ routes[i][0] + 30000, routes[i][1] + 30000 ]
        for j in range(routes[i][0], routes[i][1] + 1):
            expressway[j] += 1

    while routes:
        max_cars = max(expressway)
        max_cars_index = expressway.index(max_cars)
        will_delete = []
        for rou in routes:
            if rou[0] <= max_cars_index <= rou[1]:
                for k in range(rou[0], rou[1] + 1):
                    expressway[k] -= 1
                will_delete.append(rou)
        for delete in will_delete:
            routes.remove(delete)
        answer += 1
        
    return answer

# remove나 pop 사용할 때 하나 스킵하지 않게 하는 방법 있는지 꼭!!! 찾아보자.

solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]])