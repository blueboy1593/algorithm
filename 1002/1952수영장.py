import sys
sys.stdin = open("1952_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    voucher = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    daily = voucher[0]
    monthly = voucher[1]
    threemonth = voucher[2]
    anual = voucher[3]

    money_plan = [0] * 12
    for i in range(12):
        if plan[i]:
            a = plan[i] * daily
            b = monthly
            money_plan[i] = min(a, b)

    def DFS(i, summ):
        global save_sum
        temp_sum = summ
        for j in range(i, 10):
            three_sum = money_plan[j] + money_plan[j + 1] + money_plan[j + 2]
            if three_sum > threemonth:
                summ = temp_sum - three_sum + threemonth
                if summ < save_sum:
                    save_sum = summ
                if j + 3 <= 10:
                    DFS(j + 3, summ)            

    first_sum = sum(money_plan)
    save_sum = first_sum
    DFS(0, first_sum)

    if save_sum > anual:
        save_sum = anual
    
    print("#%d %d" %(tc, save_sum))