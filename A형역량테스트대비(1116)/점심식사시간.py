import sys
sys.stdin = open("점심식사시간_input.txt", "r")
import itertools

def count_time(arr):
    global min_count
    queue1 = []
    queue2 = []
    waiting1 = []
    waiting2 = []
    time = 0
    while arr[-1][0] > 0 and queue1 and queue2 and waiting1 and waiting2:
        time += 1
        for i in range(num_people):
            arr[i][0] -= 1
            if arr[i][0] == 0:
                if arr[i][1] == 0:
                    waiting1.append(stair1_length)
                elif arr[i][1] == 1:
                    waiting2.append(stair2_length)
        

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    room = []
    for _ in range(N):
        room.append(list(map(int, input().split())))
    min_count = 99999999
    
    # room에서 최적으로 활용할 수 있게 정보 만드는 작업
    people = []
    stairs = []
    for i in range(N):
        for j in range(N):
            if room[i][j] == 1:
                people.append((i, j))
            elif 2 <= room[i][j] <= 10:
                stairs.append((i, j, room[i][j]))
    num_people = len(people)
    people_stairs = [0] * num_people
    for i in range(num_people):
        person = people[i]
        py = person[0]
        px = person[1]
        sy0 = stairs[0][0]
        sx0 = stairs[0][1]
        dis1 = abs(py - sy0) + abs(px - sx0)
        sy1 = stairs[1][0]
        sx1 = stairs[1][1]
        dis2 = abs(py - sy1) + abs(px - sx1)
        people_stairs[i] = (dis1, dis2)

    stair1_length = stairs[0][2]
    stair2_length = stairs[1][2]
    stair_length = (stair1_length, stair2_length)

    print(people_stairs)
    print(stair_length)
    jungboksunyeol = itertools.product([0,1], repeat=num_people)
    # 여기는 중복조합 만드는 것.
    # jungbokjohab = itertools.combinations_with_replacement([0,1], num_people)
    
    for sunyeol in jungboksunyeol:
        temp = [0] * num_people
        for i in range(num_people):
            temp[i] = [people_stairs[i][sunyeol[i]], sunyeol[i]]
        temp.sort()
        print(temp)
        count_time(temp)