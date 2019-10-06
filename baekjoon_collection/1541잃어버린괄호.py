equation = input()
equation_list = []
temp = ''
for char in equation:
    if char == '-':
        equation_list.append(int(temp))
        temp = ''
        equation_list.append('-')
    elif char == '+':
        equation_list.append(int(temp))
        temp = ''
        # equation_list.append('+')
    else:
        temp += char
equation_list.append(int(temp))

result = 0
for j in range(len(equation_list)):
    if equation_list[j] == '-':
        break
    result += equation_list[j]

temp = 0
for i in range(j + 1, len(equation_list)):
    if equation_list[i] == '-':
        result -= temp
        temp = 0
    else:
        temp += equation_list[i]
result -= temp

print(result)