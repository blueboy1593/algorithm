import sys
sys.stdin = open("5185_input.txt", "r")


alph_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

def change_to_2jin(num):
    a = num // 8
    aa = num % 8
    b = aa // 4
    bb = aa % 4
    c = bb // 2
    d = bb % 2
    return str(a) + str(b) + str(c) + str(d)    

T = int(input())
for tc in range(1, T + 1):
    N, hexadecimal = input().split()
    N = int(N)
    hexa_list = list(hexadecimal)    
    result = ''
    for hexa in hexa_list:
        if hexa.isdigit():
            result += change_to_2jin(int(hexa))
        else:
            c = alph_dict.get(hexa)
            result += change_to_2jin(c)
    print("#%d %s" %(tc,result))