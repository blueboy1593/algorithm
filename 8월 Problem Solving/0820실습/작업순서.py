import sys
sys.stdin=open("input.txt", "r")

for tc in range(1,11):
    V, E = map(int,input().split())
    VE_list = list(map(int, input().split()))
    even_list=[]
    result = []
    
    veset = set(VE_list)

    for i in range(len(VE_list)):
        if i % 2 == 1:
            even_list.append(VE_list[i])
    
    while VE_list != []:
        for i in range(len(VE_list)):
            if i%2==0 and VE_list[i] not in even_list:
                a = VE_list.pop(i)
                b = VE_list.pop(i)
                even_list.remove(b)
                if a not in result:
                    result.append(a)
                if b not in result and b not in even_list:
                    result.append(b)
                break

    for j in range(1, V + 1):
        if j not in result:
            result.append(j)

    #print(V, len(result))
    str_result = ' '.join(map(str,result))
    print("#%d %s" %(tc,str_result))
    
