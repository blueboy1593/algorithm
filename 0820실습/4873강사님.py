import sys
sys.stdin=open("4873_input.txt", "r")

TC = int(input())
for tc in range(1, TC+1):
    data = list(input())
    n = len(data)   # 문자열 길이
    stack = []  # 처리할 문자를 저장할 공간
    for i in range(n):
        # 스택이 비어있거나 스택 마지막 값이 현재 처리할 값과 다른 경우
        if not stack or stack[-1] != data[i]:
            stack.append(data[i])
        elif stack and stack[-1] == data[i]:
            stack.pop() #스택 마지막글자 삭제
    print("#%d %d" %(tc, len(stack)))