def solution(n, computers):
    answer = 0
    networks = [0] * n
    stack = []
    networks_num = 0
    for i in range(n):
        if networks[i] != 0:
            continue
        else:
            networks_num += 1
            networks[i] = networks_num
            for j in range(n):
                if i != j:
                    if computers[i][j] == 1 and networks[j] == 0:
                        networks[j] = networks_num
                        stack.append(j)
            
            while stack:
                a = stack.pop(0)
                for j in range(n):
                    if a != j:
                        if computers[a][j] == 1 and networks[j] == 0:
                            networks[j] = networks_num
                            stack.append(j)

    answer = max(networks)
    return answer