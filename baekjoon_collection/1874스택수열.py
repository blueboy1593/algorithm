n = int(input())

stack1 = []
stack0 = list(range(1, n + 1))
stack2 = []
stack3 = []
num = int(input())
for i in range(1, num + 1):
    stack1.append(stack0.pop(0))
    stack2.append('+')
stack3.append(stack1.pop())
stack2.append('-')
fail = False
n_flag = False

for _ in range(n - 1):
    num = int(input())
    if n_flag == False and fail == False:
        if num == n:
            n_flag = True
        if num < stack3[-1]:
            a = stack1.pop()
            if num == a:
                stack2.append('-')
                stack3.append(num)
            elif num < a:
                fail = True
        elif num > stack3[-1]:
            while True:
                a = stack0.pop(0)
                stack1.append(a)
                stack2.append('+')
                if a == num:
                    b = stack1.pop()
                    stack2.append('-')
                    stack3.append(b)
                    break
    elif n_flag == True and fail == False:
        c = stack1.pop()   
        if c == num:
            stack2.append('-')
            stack3.append(c)
        else:
            fail = True

if fail == True:
    print("NO")
else:
    for i in range(len(stack2)):
        print(stack2[i])