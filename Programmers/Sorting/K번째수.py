# 거품정렬 정도만 해볼까?
# Quick이나 Merge도 연습을 한번정도는 해보기는 해야함.

# 시간복잡도 n^2의 가장 기본인 버블정렬
def bubble(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    return arr
# flag를 중간에 넣어주면 시간을 조금은 절약할 수 있겠다. 가지치기 개념으로?

def solution(array, commands):
    answer = []
    for comm in commands:
        a, b, c = comm
        new_arr = array[a - 1: b]
        bubbled_arr = bubble(new_arr)
        answer.append(bubbled_arr[c - 1])
    return answer