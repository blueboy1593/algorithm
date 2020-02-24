import sys
sys.stdin = open("5356_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    word_list = []
    length = 0
    result = ''
    for _ in range(5):
        temp = list(input())
        word_list.append(temp)

    for word in word_list:
        if len(word) > length:
            length = len(word)

    for i in range(length):
        for j in range(5):
            try:
                temp = word_list[j][i]
                result += temp
            except:
                pass
    print("#%d %s" %(tc,result))