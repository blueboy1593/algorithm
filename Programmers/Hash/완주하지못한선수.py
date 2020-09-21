from collections import defaultdict

def solution(participant, completion):
    answer = ''
    participant_dict = defaultdict(lambda: 0)
    for partici in participant:
        participant_dict[partici] += 1
    for comple in completion:
        participant_dict[comple] -= 1

    for key, value in participant_dict.items():
        if value == 1:
            return key