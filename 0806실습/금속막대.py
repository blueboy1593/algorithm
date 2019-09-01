import sys
sys.stdin=open("input.txt","r")

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    rod_list = list(map(int, input().split()))
    rod_len = len(rod_list)
    metal_list = []

    for i in range(rod_len):
        if rod_list.count(rod_list[i]) == 1 and i%2 ==0:
            metal_list.append(rod_list[i])
            metal_list.append(rod_list[i+1])
    
    for j in range(rod_len-1):
        for k in range(rod_len):
            if metal_list[-1] == rod_list[k] and k%2 == 0:
                metal_list.append(rod_list[k])
                metal_list.append(rod_list[k+1])
    
    print("#%d " %tc + ' '.join(map(str, metal_list)))
