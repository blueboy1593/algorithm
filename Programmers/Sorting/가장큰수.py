# 이문제 재밌어보인다. 저번에 어디서 본거같은데?

def solution(numbers):
    answer = ''
    n_numbers = []
    for number in numbers:
        str_number = str(number)
        if len(str_number) < 4:
            str_number = str_number.ljust(4, '-')
        n_numbers.append(str_number)
    print(n_numbers)

    new_numbers = sorted(n_numbers, key=lambda x: (x[0], x[1], x[2], x[3]), reverse=True)
    print(new_numbers)
    return answer

solution([3, 30, 34, 5, 9])
# 이 문제는 다음에 다시!! 졸리다.