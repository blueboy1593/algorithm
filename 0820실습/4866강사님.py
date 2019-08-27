
import sys
sys.stdin=open("4866_input.txt", "r")

TC = int(input())
for tc in range(1, TC + 1):
    data = input()
    mystack = []
    for i in range( len(data )):
        if data[i] == "(" or data[i] == "{":
            mystack.append(data[i])
        elif data[i] == ")" or data[i] == "}":
            if len(mystack)== 0:
                mystack[data[i]]
                break

            elif (data[i] == ")" and mystack[-1] != '(') or (data[i]=="}" and mystack[-1] != "{"):
                mystack.append(data[i])
                break
            else:
                mystack.pop()

    if len(mystack)==0 :
        print("#%s %s" %(tc, 1)) #바른문장
    else:
        print("#%s %s" %(tc, 0))