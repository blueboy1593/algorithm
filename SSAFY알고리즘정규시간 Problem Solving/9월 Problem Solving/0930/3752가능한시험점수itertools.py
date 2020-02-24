import sys
sys.stdin = open("3752_input.txt", "r")
import itertools

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    grade = list(map(int, input().split()))
    grade_set = set()
    for i in range(0, N + 1):
        grade_comb = itertools.combinations(grade, i)
        for comb in grade_comb:
            a= sum(comb)
            grade_set.add(a)
    result = len(grade_set)

    print("#%d %d" %(tc, result))