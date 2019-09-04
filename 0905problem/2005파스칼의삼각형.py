import sys
sys.stdin = open("2005_input.txt", "r")

def pascal(n):
    if n == 1:
        temp = [1]
        return temp
    elif n == 2:
        temp = [1, 1]
        return temp
    else:
        temp = [1]
        for i in range(n - 2):
            pasca = pascal(n-1)
            temp_value = pasca[i] + pasca[i + 1]
            temp.append(temp_value)
        temp.append(1)
        return temp 

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    result = [0] * N
    for y in range(N):
        result[y] = ' '.join(map(str, pascal(y + 1)))
    
    print("#%d" %tc)
    for i in range(N):
        print(result[i])