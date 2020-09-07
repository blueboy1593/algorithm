def solution(numbers, target):
    value_list = [ 0 ]
    for num in numbers:
        value_list2 = []
        for value in value_list:
            value_list2.append(value + num)
            value_list2.append(value - num)
        value_list = value_list2
    answer = value_list.count(target)
    return answer