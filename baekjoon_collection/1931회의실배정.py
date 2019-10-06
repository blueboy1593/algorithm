N = int(input())

# conference_time = [0] * (2**31)
time1 = []
time2 = []
length = 0
for _ in range(N):
    a, b = map(int, input().split())
    if b > length:
        length = b
    if a == b:
        time2.append(a)
    else:
        time1.append([a, b])

conference_time = [0] * (length + 1)
for time11 in time1:
    for i in range(time11[0], time11[1]):
        conference_time[i] += 1

for time22 in time2:
    conference_time[time22] += 1

print(max(conference_time))