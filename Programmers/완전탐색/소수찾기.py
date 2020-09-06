def IF_prime_or_not(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    numbers_list = list(numbers)

    # 순열이 필요한데, 생각나는데로 해보자.
    number_leng = len(numbers_list)
    TF = [False] * number_leng
    number_stack = []
    answer_dict = {}
    
    def sunyeol():
        for i in range(number_leng):
            if TF[i] == False:
                TF[i] = True
                number_stack.append(numbers_list[i])
                # print(number_stack) 내가 원하던 순열 잘 뽑히는거 확인
                prime_check_num = int(''.join(number_stack))
                if IF_prime_or_not(prime_check_num):
                    answer_dict[prime_check_num] = 1
                sunyeol()
                number_stack.pop()
                TF[i] = False
    sunyeol()
    return len(answer_dict)


solution("011")