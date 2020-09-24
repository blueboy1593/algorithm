def solution(money):
    answer = 0
    len_money = len(money)
    DP = [0] * len_money
    DP[1] = money[1]
    DP[2] = money[2]
    for i in range(3, len_money):
        DP[i] = max(DP[i - 2], DP[i - 3]) + money[i]

    DP2 = [0] * len_money
    DP2[0] = money[0]
    DP2[2] = money[2] + money[0]
    for j in range(3, len_money - 1):
        DP2[j] = max(DP2[j - 2], DP2[j - 3]) + money[j]

    answer = max(DP[-1], DP[-2], DP2[-3], DP2[-2])
    return answer