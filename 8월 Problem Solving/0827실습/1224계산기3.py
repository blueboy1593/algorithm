import sys
sys.stdin = open("1224_input.txt", "r")

def calcul(lis):
    calcul_stack=[]
    for i in range(len(lis)):
        if type(lis[i])==int:
            calcul_stack.append(lis[i])
        elif lis[i]=="+":
            a = int(calcul_stack.pop())
            calcul_stack[-1] = calcul_stack[-1] + a
        elif lis[i]=="-":
            b = int(calcul_stack.pop())
            calcul_stack[-1] = calcul_stack[-1] - b
        elif lis[i]=="*":
            c = int(calcul_stack.pop())
            calcul_stack[-1] = calcul_stack[-1] * c
        elif lis[i]=="/":
            d = int(calcul_stack.pop())
            calcul_stack[-1] = calcul_stack[-1] / d
    return calcul_stack[0]

T = 10

for tc in range(1, T+1):
    N=int(input())
    data = list(input())
    stack_num=[]
    stack_kiho=[]

    for i in range(N):
        if data[i].isdigit():
            stack_num.append(int(data[i]))
        elif data[i] == "+" or data[i] == "-":
            while stack_kiho[-1] == "*" or stack_kiho[-1] == "/":
                bb = stack_kiho.pop()
                stack_num.append(bb)
            stack_kiho.append(data[i])
        elif data[i] == "*" or data[i] == "/":
            while stack_kiho[-1] == "*" or stack_kiho[-1] == "/":
                bb = stack_kiho.pop()
                stack_num.append(bb)
            stack_kiho.append(data[i])
        elif data[i] == "(":
            stack_kiho.append(data[i])
        elif data[i] == ")":
            while True:
                aa = stack_kiho.pop()
                if aa == "(":
                    break
                else:
                    stack_num.append(aa)
    #print(stack_num)
    result = calcul(stack_num)
    print("#%d %d" %(tc,result))