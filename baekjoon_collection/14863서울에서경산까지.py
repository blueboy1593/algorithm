import itertools
import time
st = time.time()

N, K = map(int, input().split())

jasun_trip = [0] * N
for i in range(N):
    a, b, c, d = map(int, input().split())
    jasun_trip[i] = [ [a, b], [c, d] ]

walk_or_bike = [0, 1]
route_list = itertools.product(walk_or_bike, repeat=N)
maxmax = 0

def fund_raising(route):
    global maxmax
    time = 0
    money = 0
    for i in range(N):
        fund = jasun_trip[i][route[i]]
        time += fund[0]
        money += fund[1]
        if time > K:
            return
    if money > maxmax:
        maxmax = money

for route in route_list:
    fund_raising(route)

print(maxmax)
print(time.time() - st)