
def gwalho(word):
    stack = []
    for char in word:
        if char == '(':
            stack.append(char)
        elif char == ')':
            stack.pop()
    if stack == []:
        return True
    else:
        return False

a = gwalho('((((((((())))')
print(a)
