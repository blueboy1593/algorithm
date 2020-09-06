# 최대공약수 사용해서 푸는 것. 이거까진 생각 못함...

import math
def solution(w,h):
    return w*h - (w+h-math.gcd(w,h))