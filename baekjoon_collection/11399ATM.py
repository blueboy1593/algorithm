N = int(input())

atm_time = list(map(int, input().split()))

atm_time.sort()

result = 0
for i in range(N):
    time = N - i
    result += time * atm_time[i]

print(result)