N = int(input())
TP_list = [[0, 0]]
for i in range(N):
    temp = list(map(int, input().split()))
    TP_list.append(temp)
money_list = []
money = 0

def goout(i, money, visited):
    # if i == N:
    #     return
    if visited[i] == False:
        a = TP_list[i][0]
        b = TP_list[i][1]
        for j in range(a):
            if i + j > N:
                money_list.append(money)
                return
            visited[i + j] = True
        money += b
        print(money)
        k = i + a
        while True:
            if k > N:
                money_list.append(money)
                break
            goout(k, money, visited)
            k += 1
    else:
        return
for m in range(1, N+1):
    visited = [False] * (N + 1)
    money = 0
    goout(m, money, visited)
print(money_list)
result = max(money_list)
print(result)