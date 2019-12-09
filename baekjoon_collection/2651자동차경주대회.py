import sys
sys.setrecursionlimit(100000)

distance = int(input())
num_of_garage = int(input())
interval_list = [0] + list(map(int, input().split()))
garage_time = [0] + list(map(int, input().split())) + [0]
interval_length = len(interval_list)

def car_go(i, time):
    global min_time, check_list
    if time > min_time:
        return
    elif i == interval_length - 1:
        if time < min_time:
            min_time = time
            check_list = TF[:]
        return
    else:
        nujuk = 0
        for j in range(i + 1, interval_length):
            nujuk += interval_list[j]
            if nujuk <= distance:
                TF[j] = True
                car_go(j, time + garage_time[j])
                TF[j] = False
            else:
                return

if sum(interval_list) <= distance:
    print('0')
    print('0')
else:
    min_time = 9999
    check_list = []
    nujuk = 0
    for i in range(1, len(interval_list)):
        nujuk += interval_list[i]
        if nujuk <= distance:
            TF = [False] * (interval_length)
            TF[i] = True
            car_go(i, garage_time[i])
        else:
            break
    check_list.pop()
    print(min_time)
    cnt = 0
    result = []
    for i in range(len(check_list)):
        if check_list[i] == True:
            cnt += 1
            result.append(i)
    print(cnt)
    print(' '.join(map(str,result)))