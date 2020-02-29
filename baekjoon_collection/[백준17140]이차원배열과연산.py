r, c, K = map(int, input().split())
r -= 1
c -= 1
arrangement = [ list(map(int, input().split())) for _ in range(3) ]
big_arr = [ [ 0 ] * 100 for _ in range(100) ]
for i in range(3):
    for j in range(3):
        big_arr[i][j] = arrangement[i][j]
# print(*big_arr, sep='\n')

time = 0
while time < 101:
    # 종료 조건!
    # print('r, c', r, c)
    # print(big_arr[r][c], k)

    # 소문자 쓰지 말자.... ㅠㅠㅠㅠㅠㅠㅠㅠ
    if big_arr[r][c] == K:
        break
    
    # R연산 , C연산 중에 뭐 할지 고르기. 노가다같기는 하지만 그냥 해.
    r_length = 100
    for i in range(100):
        if sum(big_arr[i]) == 0:
            r_length = i
            break
    c_length = 100
    for j in range(100):
        sumsum = 0
        for i in range(100):
            sumsum += big_arr[i][j]
        if sumsum == 0:
            c_length = j
            break

    # 이 문제 list로 풀면 훨씬 쉬울 것 같은데, 연습할 겸 dict로 풀자.
    # nums = [ j for j in range(1, 101) ]
    # print(nums)
    # record_dict = { j : 0 for j in range(1, 101) }
    # print(record_dict)
    # 이거만 해도 이번 문제 성공

    # R연산 조건!
    if r_length >= c_length:
        for i in range(r_length):
            will_count = big_arr[i]
            # 가지치기! 이 가지치기는 빼야 할듯
            # if will_count[0] == 0:
            #     break
            # 딕셔너리에 기록하기
            record_dict = { j : 0 for j in range(1, 101) }
            for k in range(100):
                if will_count[k] != 0: # 가지치기 하다가 골로 가는겨
                    record_dict[will_count[k]] += 1 # 이거 되나...?
            # 다시 만드는 로직
            # i2 = 0
            new_arr = [0] * 100
            my_tuple = []
            for k2 in range(1, 101):
                if record_dict.get(k2) != 0:
                    my_tuple.append((record_dict[k2], k2))
                    # new_arr[i2] = k2
                    # new_arr[i2 + 1] = record_dict[k2]
                    # i2 = i2 + 2
                    # if i2 >= 100:
                    #     break
            my_tuple.sort()
            # 조금은 error 가능성
            tuple_len = len(my_tuple)
            for i2 in range(min(50, tuple_len)):
                val, keyy = my_tuple[i2]
                i3 = i2 * 2
                new_arr[i3] = keyy
                new_arr[i3 + 1] = val
            # 이거는 진짜 실력 향상 인건가??
            big_arr[i] = new_arr
    # C연산 조건!
    else:
        # J 건드리면 안됨
        for J in range(c_length):
            will_count = [0] * 100
            for i in range(100):
                # 가지치기 2 얘도 빼야하뮤
                # if big_arr[i][J] == 0:
                #     break
                # else:
                will_count[i] = big_arr[i][J]    
            # 가지치기!
            # if will_count[0] == 0:
            #     break
            record_dict = { j : 0 for j in range(1, 101) }
            for k in range(100):
                if will_count[k] != 0:
                    record_dict[will_count[k]] += 1
            new_arr = [0] * 100
            my_tuple = []
            for k2 in range(1, 101):
                if record_dict.get(k2) != 0:
                    my_tuple.append((record_dict[k2], k2))
            my_tuple.sort()
            # 조금은 error 가능성
            tuple_len = len(my_tuple)
            for i2 in range(min(50, tuple_len)):
                val, keyy = my_tuple[i2]
                i3 = i2 * 2
                new_arr[i3] = keyy
                new_arr[i3 + 1] = val
            # 여기는 또 여기만의 로직
            
            for i in range(100):
                big_arr[i][J] = new_arr[i]
    # print(*big_arr, sep='\n')
    # print('---------------------------------------------------------------------')
    time += 1

if time == 101:
    time = -1
print(time)
# 1시간 20분