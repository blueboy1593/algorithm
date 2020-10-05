def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    dele = []
    for lo in lost:
        if lo in reserve:
            dele.append(lo)
    for de in dele:
        lost.remove(de)
        reserve.remove(de)
    
    answer = 0
    TF = [ False ] + [ True ] * n
    for lo in lost:
        for re in reserve:
            if abs(re - lo) <= 1:
                reserve.remove(re)
                break
        else:
            TF[lo] = False
    answer = TF.count(True)
    return answer