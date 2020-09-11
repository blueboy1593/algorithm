# return값(시행 횟수)에 초점을 맞춰서 하는 DP 작업

def solution(N, number):
    DPDP = [0, {N}]
    # 테스트케이스 9번
    if number == N:
        return 1

    for i in range(2, 9):
        DP_cases = {int(str(N)*i)}
        for ih in range(1, i//2 + 1):
            for a in DPDP[ih]:
                for b in DPDP[i - ih]:
                    DP_cases.add(a + b)
                    DP_cases.add(a - b)
                    DP_cases.add(b - a)
                    DP_cases.add(a * b)
                    if a != 0:
                        DP_cases.add(b // a)
                    if b != 0:
                        DP_cases.add(a // b)
        if number in DP_cases:
            return i
        DPDP.append(DP_cases)
    return -1