from collections import defaultdict

def solution(clothes):
    answer = 1
    clothes_dict = defaultdict(list)
    for cloth in clothes:
        a, b = cloth
        clothes_dict[b].append(a)
    
    arr = []
    for value in clothes_dict.values():
        arr.append(len(value))

    for ar in arr:
        answer *= ar + 1
    answer -= 1

    return answer

solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']])