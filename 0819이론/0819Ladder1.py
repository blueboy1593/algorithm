import sys
sys.stdin=open("input.txt","r")

for tc in range(1, 11):
    N = int(input())
    total_list = []
    right = False
    going = False
    
    for i in range(100):
        total_list.append(list(map(int, input().split())))

    for j in range(100):
        if total_list[99][j] == 2:
            x = j
            y = 99
    
    for i in range(1000):
        if y == 0:
            result = x
            break
        else:
            if x >= 1 and x <= 98:
                if total_list[y][x+1] == 1 and total_list[y][x-1] == 0:
                    if going == True:
                        y -= 1
                        going = False
                    else:
                        x += 1
                        right = True
                elif total_list[y][x-1] == 1 and total_list[y][x+1] == 0:
                    if going == True:
                        y -= 1
                        going = False
                    else:
                        x -= 1
                        right = False
                elif total_list[y][x+1] == 1 and total_list[y][x-1] == 1:
                    if right == True:
                        x +=1
                        going = True
                    else:
                        x -=1
                        going = True
                else:
                    y -= 1 
            elif x == 0:
                if total_list[y][x+1] == 1:
                    if going == True:
                        y -= 1
                        going = False
                    else:
                        x += 1
                        right = True
                else:
                    y -= 1
            elif x == 99:
                if total_list[y][x-1] == 1:
                    if going == True:
                        y -= 1
                        going = False
                    else:
                        x -= 1
                        right = False
                else: y -= 1
    
    print('#%d %d' %(N,result))

