N = int(input())

chinmok = []
while True:
    a, b = map(int, input().split())
    # -1 -1을 괜히 준거는 아니구나!!!
    if a == -1 and b == -1:
        break
    chinmok.append(a)
    chinmok.append(b)
near_president = {}
for key in chinmok:
    near_president[key] = 0

# chinmok 리스트 다룰 때 좀 더 편한 방법 있는지 찾아보자. 튜플 딕 등등 뭘로 하는게 좋을지? dic도 괜찮은듯하고.
def checkBFS(num, visited, queue):
    for i in range(len(chinmok)):
        if chinmok[i] == num and i%2 == 0:
            if visited[chinmok[i+1]] == False:
                queue.append(chinmok[i+1])
                visited[chinmok[i+1]] = True
        if chinmok[i] == num and i%2:
            if visited[chinmok[i-1]] == False:
                queue.append(chinmok[i-1])
                visited[chinmok[i-1]] = True

def president(num):
    visited = [False]*(len(near_president)+1)
    queue = [num]
    visited[num] = True
    cnt = -1
    while queue:
        cnt += 1
        for j in range(len(queue)):
            num1 = queue.pop(0)
            checkBFS(num1, visited, queue)
    near_president[num] = cnt
    return

for key in near_president.keys():
    president(key)

min_value = min(near_president.values())
count = 0
president_list = []
for key, value in near_president.items():
    if value == min_value:
        president_list.append(key)
        count += 1

president_list.sort()
president_list = ' '.join(map(str, president_list))
print("%d %d" %(min_value, count))
print(president_list)