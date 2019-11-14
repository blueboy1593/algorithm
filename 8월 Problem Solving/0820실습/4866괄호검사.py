import sys
sys.stdin=open("sample_input.txt", "r")

T=int(input())

for tc in range(1,T+1):
    word_list=list(input())
    gwalho_list=[]
    for word in word_list:
        if word == '{' or word == '}' or word == '(' or word == ')':
            gwalho_list.append(word)
    
    result = 0
    
    for j in range(len(gwalho_list)):
        if gwalho_list == []:
            result = 1
            break
        for i in range(len(gwalho_list)-1):
            if gwalho_list[i] == '(' and gwalho_list[i+1] == ')':
                gwalho_list.pop(i)
                gwalho_list.pop(i)
                break
            elif gwalho_list[i] == '{' and gwalho_list[i+1] == '}':
                gwalho_list.pop(i)
                gwalho_list.pop(i)
                break
    print("#%d %d" %(tc,result))
