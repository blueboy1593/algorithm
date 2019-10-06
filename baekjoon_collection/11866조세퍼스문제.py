N, K = map(int, input().split())
josephers = list(range(1, N + 1))

result = []
i = K - 1
n = N - 1
while len(josephers) > 0:
    a = josephers.pop(i)
    result.append(a)
    i += K - 1
    if i > n:
        i = i%n
    n -= 1

poppop = josephers.pop(0)
result.append(poppop)
print('<', end = '')
print(','.join(map(str,result)), end= '')
print('>')