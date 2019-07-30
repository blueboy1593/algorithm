nosunsu = int(input())
KNM_list = []
station_num_list = []

for nosun in range(nosunsu):
    KNM = list(map(int, input().split()))
    station_num = list(map(int, input().split()))
    KNM_list.append(KNM)
    station_num_list.append(station_num)

def find_short(KNM):
    K = KNM[0]
    N = KNM[1]
    M = KNM[2]
    

print(KNM_list)
print(station_num_list)


