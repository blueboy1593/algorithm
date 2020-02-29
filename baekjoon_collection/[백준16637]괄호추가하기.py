# from itertools import combinations_with_replacement, product

N = int(input())
susik = list(input())
n = N//2
# operator_list = list(combinations_with_replacement([0, 1], n)) 좋은 연습이었다.
# operator_list = list(product((0, 1), repeat=n)) # 이거다 이거다! 괄호가 연속해서 있을 수 없기에 새로 만들어야 함.
max_value = -(2**31) # 이거 생각이...
operator_list = []
# 수식의 정수화
for i in range(N):
    if not i % 2:
        susik[i] = int(susik[i])

def make_product(arr, cnt):
    if cnt == n:
        operator_list.append(arr[:])
        return
    if arr[-1] == 0:
        for i in range(2):
            make_product(arr + [i], cnt + 1)
    elif arr[-1] == 1:
        make_product(arr + [0], cnt + 1)

# N == 1 N == 1 N == 1 N == 1 N == 1
# N == 1 N == 1 N == 1 N == 1 N == 1
# N == 1 N == 1 N == 1 N == 1 N == 1
if n >= 1:
    make_product([0], 1)
    make_product([1], 1)
else:
    max_value = susik[0]
# print(operator_list) 이제 금방 금방 되네!!

def calcul(oper , a, b):
    if oper == '+':
        return a + b
    elif oper == '-':
        return a - b
    elif oper == '*':
        return a * b

for operator in operator_list:
    temp_susik = [susik[0]]
    for i in range(1, N):
        # 연산자일 때
        if i % 2:
            index = i//2
            op = susik[i]
            next_num = susik[i + 1]
            if operator[index] == 1: # 괄호!
                temp_susik[-1] = calcul(op, temp_susik[-1], next_num)
            else: # 괄호 없기
                temp_susik.append(op)
                temp_susik.append(next_num) # 이렇게 해도 돼!
    value = temp_susik[0]
    # print(temp_susik)
    for j in range(1, len(temp_susik)):
        if j % 2:
            value = calcul(temp_susik[j], value, temp_susik[j + 1])
    max_value = max(value, max_value)

print(max_value)