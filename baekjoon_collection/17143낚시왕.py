# import sys
# sys.stdin=open("17143_input.txt", "r")

R, C, M = map(int, input().split())
shark = []
for i in range(M):
    temp = list(map(int, input().split()))
    shark.append(temp)
pan = [ [0]*(C+1) for _ in range(R+1) ]
fisher = 0
catch = 0

def move(pin):
    global R, C
    y = pin[0]
    x = pin[1]
    s = pin[2]
    d = pin[3]
    for i in range(s):
        if d == 1:
            y -= 1
        if d == 2:
            y += 1
        if d == 3:
            x += 1
        if d == 4:
            x -= 1

        if x == C:
            x = C - 2
            d = 4
        if x == 0:
            x = 2
            d = 3
        if y == R:
            y = R - 2
            d = 1
        if y == 0:
            y = 2
            d = 2
    pin[0] = y
    pin[1] = x
    return pin

def battle(a, b):
    if a[4] > b[4]:
        b = 0
        return a
    elif a[4] <= b[4]:
        a = 0
        return b

for i in range(M):
    pan[shark[i][0]][shark[i][1]] = shark[i]

print(pan)
for i in range(C):
    fisher += 1
    for j in range(R+1):
        if pan[j][i+1] != 0:
            print(pan[j][i+1])
            catch += pan[j][i+1][4]
            pan[j][i+1] = 0
            break
    # print(pan)
    for k in range(R+1):
        for l in range(C+1):
            if pan[k][l] != 0:
                # print(pan[k][l])
                b = move(pan[k][l])
                # print(b)

                if pan[b[0]][b[1]] == 0:
                    pan[b[0]][b[1]] = b
                    pan[k][l] = 0
                    # print(pan)
                elif pan[b[0]][b[1]] == b:
                    pass
                else:
                    c = battle(pan[b[0]][b[1]], b)
                    # print(c)
                    pan[c[0]][c[1]]= c
                    pan[k][l] = 0
                    # print(pan)

print(pan)
print(catch)
