# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# A를 건드리지 않아도 된다는 조건이 생각보다 어렵네.

def solution(name):
    answer = -1
    joystick_dict = { 'A': 0, 'B': 1, 'Z':1, 'C': 2, 'Y': 2, 'D': 3, 'X': 3, 'E': 4, 'W': 4, 'F': 5, 'V':5, 'G':6, 'U':6, 'H':7, 
    'T': 7, 'I':8, 'S':8, 'J': 9, 'R':9, 'K':10, 'Q':10, 'L':11, 'P': 11, 'M':12, 'O':12, 'N': 13 }

    # 1번. 조이스틱 위아래로 조작하기
    for i in range(len(name)):
        answer += joystick_dict[name[i]]

    # 2번. 조이스틱 좌우로 조작하기
    # Linked List 개념으로
    stack1 = 0
    for j in range(1, len(name)):
        if name[j] == 'A':
            stack1 += 1
        else:
            break

    stack2 = 0
    for k in range(len(name) - 1, 0, -1):
        if name[k] == 'A':
            stack2 += 1
        else:
            break
    max_stack = max(stack1, stack2)
    answer += len(name) - max_stack

    return answer

print(solution('BBBAAAB'))
print(solution('ABABAAAAABA'))