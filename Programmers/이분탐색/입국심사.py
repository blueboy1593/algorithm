def solution(n, times):
    l_pivot = 0
    r_pivot = 10000000000000 # 이 숫자에 대해서는 조건을 좀 더 생각해볼 필요가 있다.
    while l_pivot + 1 < r_pivot:
        m_pivot = (l_pivot + r_pivot) // 2
        screening = 0
        flag = False
        for i in range(len(times)):
            screening += m_pivot // times[i]
            if screening >= n:
                flag = True
                break
        
        # 충족된다면 right pivot 옮기기
        if flag == True:
            r_pivot = m_pivot
        else:
            l_pivot = m_pivot
    return r_pivot

solution(6,[7, 10])