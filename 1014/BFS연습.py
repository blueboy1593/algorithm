gansun = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

gan_dict = {}
for i in range(len(gansun)):
    if i % 2 == 0:
        if gansun[i] in gan_dict.keys():
            gan_dict[gansun[i]].append(gansun[i + 1])
        else:
            gan_dict[gansun[i]] = [gansun[i + 1]]

visited = [False] * 8
visited[1] = True
queue = [1]
result = [1]
while queue:
    for _ in range(len(queue)):
        a = queue.pop(0)
        if a in gan_dict.keys():
            for b in gan_dict[a]:
                if visited[b] == False:
                    queue.append(b)
                    result.append(b)
                    visited[b] = True
print(result)