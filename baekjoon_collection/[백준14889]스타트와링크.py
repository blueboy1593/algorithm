N = int(input())
S = []
for _ in range(N):
  S.append(list(map(int, input().split())))
# print(*S, sep='\n')
min_chai = 99999999

def startlink(i, cnt):
  global min_chai
  if cnt == N//2:
    start = []
    link = []
    for sl in range(N):
      if visited[sl] == True:
        start.append(sl)
      else:
        link.append(sl)
    start_power = sum_power(start)
    link_power = sum_power(link)
    # print(start, link)
    power_chai = abs(start_power - link_power)
    min_chai = min(power_chai, min_chai)
    return
  for j in range(i + 1, N):
    visited[j] = True
    startlink(j, cnt + 1)
    visited[j] = False

def sum_power(team):
  power = 0
  for i in range(N//2):
    for j in range(i + 1,N//2):
      power += S[team[i]][team[j]]
      power += S[team[j]][team[i]]
  return power

for s in range(N//2 + 1):
  visited = [ False ] * N
  visited[s] = True
  startlink(s, 1)

print(min_chai)