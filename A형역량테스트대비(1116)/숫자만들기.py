import sys
sys.stdin = open("숫자만들기_input.txt", "r")


# 백트래킹 하던거 응용해서 중복순열 만들기
def make_repeated_permu(permu, cnt):
    if cnt == oper_length:
        # print(permu)
        permu_list.append(permu[:])
        return
    cnt += 1
    for i in range(4):
        if operator[i] > 0:
            operator[i] -= 1
            permu.append(i)
            make_repeated_permu(permu, cnt)
            operator[i] += 1
            permu.pop()


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    operator = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    
    # 중복순열 만드는 함수와 초기값 설정
    permu_list = []
    permu = []
    cnt = 0
    oper_length = sum(operator)
    make_repeated_permu(permu, cnt)

    # 연산자 계산해주는 것. //= 같은 것도 사용 가능하다.
    value_list = []
    calculate_num = len(numbers) - 1
    for permu in permu_list:
        value = numbers[0]
        for n in range(calculate_num):
            if permu[n] == 0:
                value += numbers[n + 1]
            elif permu[n] == 1:
                value -= numbers[n + 1]
            elif permu[n] == 2:
                value *= numbers[n + 1]
            elif permu[n] == 3:
                if value >= 0:
                    value //= numbers[n + 1]
                ############################################
                # 여기 나누기 하는 부분이 제일 중요.
                # 음수일때는 양수로 바꿔서 해준다음에 다시 음수로 바꿔주기.
                else:
                    value = -((-value)//numbers[n + 1])
        value_list.append(value)

    # max랑 min 제대로 되겠지?
    result = max(value_list) - min(value_list)
    print("#%d %d" %(tc, result))