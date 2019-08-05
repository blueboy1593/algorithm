nosunsu = int(input())

for nosun in range(1,nosunsu + 1):
    KNM = list(map(int, input().split()))
    station_num = list(map(int, input().split()))
    
    K = KNM[0] # 한번 충전으로 갈 수 있는 거리
    N = KNM[1] # 종점까지의 거리
    M = KNM[2] # 충전기의 갯수
    charge_count = 0
    bus = K
    bus_moved = 0
    error = False
    for j in range(len(station_num)-1):
        if (station_num[j+1] - station_num[j]) > K:
            error = True
    if error != True:
        while bus < N:
            for charger in station_num:
                if bus >= charger:
                    bus_moved = charger
            charge_count += 1
            bus = bus_moved + K
    else: charge_count = 0
    print('#%d %d' %(nosun,charge_count))

# KNM_list = []
# station_num_list = []
# KNM_list.append(KNM)
# station_num_list.append(station_num)
# print(KNM_list)
# print(station_num_list)
