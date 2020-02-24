import sys
sys.stdin=open("4874_input.txt", "r")

def som(least):
    try:
        a = int(least.pop())
        least[-1] = least[-1] + a
        return least
    except IndexError:
        return False

def gob(least):
    try:
        b = int(least.pop())
        least[-1] = least[-1] * b
        return least
    except IndexError:
        return False

def bbagi(least):
    try:
        g = int(least.pop())
        least[-1] = least[-1] - g
        return least
    except IndexError:
        return False

def nanugi(least):
    try:
        h = int(least.pop())
        least[-1] = int(least[-1]/h)
        return least
    except IndexError:
        return False

T=int(input())
for tc in range(1, T+1):
    sic = list(input().split())
    num_stack=[]

    for wo in sic:
        if wo == '.':
            try:
                if len(num_stack) > 1:
                    result='error'
                else:
                    result=int(num_stack.pop())
            except ValueError:
                result='error'
            break
        elif wo == "+":
            c = som(num_stack)
            if c==False:
                result='error'
                break
        elif wo == "*":
            d = gob(num_stack)
            if d==False:
                result='error'
                break
        elif wo == "-":
            e = bbagi(num_stack)
            if e==False:
                result='error'
                break
        elif wo == "/":
            f = nanugi(num_stack)
            if f==False:
                result='error'
                break
        else:
            num_stack.append(int(wo))
    result = str(result)
    print("#%d %s" %(tc, result))