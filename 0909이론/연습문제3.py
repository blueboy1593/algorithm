jinsoo = input()

# replace를 사용해서 바꿔줄 수 있다.
final_sum = ''
for i in range(len(jinsoo)):
    if jinsoo[i] == "F":
        temp = 15
    elif jinsoo[i] == "E":
        temp = 14
    elif jinsoo[i] == "D":
        temp = 13
    elif jinsoo[i] == "C":
        temp = 12
    elif jinsoo[i] == "B":
        temp = 11
    elif jinsoo[i] == "A":
        temp = 10
    else:
        temp = int(jinsoo[i])
    a = temp // 8
    aa = temp % 8
    b = aa // 4
    bb = aa % 4
    c = bb // 2
    d = bb % 2
    final = str(a) + str(b) + str(c) + str(d)
    final_sum += final
print(final_sum)