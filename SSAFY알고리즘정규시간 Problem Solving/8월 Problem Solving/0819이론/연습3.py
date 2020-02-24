visited = [False] * 8
original_list = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
adjacent_list = [[],[],[],[],[],[],[],[]]
# print(adjacent_list)

for i in range(len(original_list)):
    if i % 2 == 0:
        adjacent_list[original_list[i]].append(original_list[i+1])
    else:
        adjacent_list[original_list[i]].append(original_list[i-1])

for i in range(len(adjacent_list)):
    adjacent_list[i].reverse()
    
print(adjacent_list)
print(visited)

stack = [1]
result = []

while True:
    if visited.count(True) == 7:
        break
    temp = stack.pop()
    
    if visited[temp] == False:
        
        result.append(temp)
        visited[temp] = True
        stack += adjacent_list[temp]

    print(temp)
    print(stack)
    print(result)
    





