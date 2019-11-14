import sys
sys.stdin = open("5099_input.txt", "r")

def pushpull(ex):
    ex.append(ex.pop(0))
    return

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))
    pizza =  [ [i+1, Ci[i]] for i in range(M)]
    queue = []
    # print(pizza)
    queue.append(pizza.pop(0))

    while queue:
        while len(queue) < N:
            if pizza == []:
                break
            piece = pizza.pop(0)
            queue.append(piece)

        for i in range(len(queue)):
            queue[0][1] = queue[0][1]//2
            if queue[0][1] == 0:
                queue.pop(0)
                if pizza != []:
                    queue.append(pizza.pop(0))
            else:
                pushpull(queue)
            if len(queue) == 1:
                result = queue[0][0]

    print('#' + str(tc) + ' ', end='')
    print(result)