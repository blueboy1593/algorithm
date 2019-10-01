import sys
sys.stdin = open('1238_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    length, start = map(int, input().split())
    fake_node_list = list(map(int, input().split()))
    node_list = []
    for i in range(0, length, 2):
        node_list.append(fake_node_list[i:i+2])

    queue = []
    for i in range(length//2):
        if node_list[i][0] == start:
            queue.append(node_list[i])

    last_nodes = []
    def bfs():  # s = 방문하는 간선
        node_visited = [start]
        while queue:
            last_nodes = []
            for _ in range(len(queue)):
                a = queue.pop(0)
                for i in range(length // 2):
                    if node_list[i][0] == a[1] and node_list[i][1] not in node_visited:
                        node_visited.append(a[1])
                        last_nodes.append(a[1])
                        queue.append(node_list[i])

        # print(node_visited)
    bfs()
    print(last_nodes)
    max_res = 0
    for i in range(len(last_nodes)):
        if max_res < last_nodes[i]:
            max_res = last_nodes[i]
    #print('#{} {}'.format(tc, max_res))