import sys
sys.stdin = open("4874_input.txt", "r")

TC = int(input())

for tc in range(1, TC+1):
    data = list(input().split())
    n = len(data)   # 반복 횟수
    stack=[]
    result = 0
    errorFlag = False

    for i in range(n-1):  # 연산식 만큼 반복
        # 숫자이면 스택에 저장
        try:
            if data[i].isdigit():   # 숫자인지?
                stack.append(data[i])
            else:   # 숫자가 아니면
                # 후위표기법 계산   # 마지막 이전숫자 "연산자" 마지막숫자
                num2, num1 = int(stack.pop()), int(stack.pop())
                if data[i] == "+": result=num1+num2
                elif data[i] == "-": result = num1 - num2
                elif data[i] == "*": result = num1 * num2
                elif data[i] == "/": result = num1 // num2
                # 계산결과를 스택에 저장
                stack.append(result)
        except:
            errorFlag = True
        #for 끝
    if errorFlag == False and len(stack)==1:
        print("#%d %d" %(tc, stack[0]))
    elif errorFlag == True or len(stack) > 1:
        print("#%d error" %tc)
    # 숫자 출력할 때 %s로 사용해도 된다.
    # 강사님은 출력할 때 무조건 %s로 하신다고 한다.