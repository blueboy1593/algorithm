from collections import defaultdict

def solution(tickets):
    answer = []
    tickets_dict = defaultdict(list)
    for st, end in tickets:
        tickets_dict[st].append(end)
    answer.append('ICN')
    real_answer = []
    len_tickets = len(tickets)

    def backtracking(airport):
        if tickets_dict[airport]:
            # 여기서 sort과정 삑사리 날거같은데...?
            tickets_dict[airport].sort()
            for i in range(len(tickets_dict[airport])):
                destination = tickets_dict[airport].pop(i)
                answer.append(destination)
                backtracking(destination)
                answer.pop()
                tickets_dict[airport].insert(i, destination)
        else:
            if real_answer == [] and len(answer) == len_tickets + 1:
                real_answer.append(answer[:])
            return
    backtracking('ICN')
    return real_answer[0]

solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']])