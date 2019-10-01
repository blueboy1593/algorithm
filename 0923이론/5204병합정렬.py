import sys
sys.stdin = open("5204_input.txt", "r")

T = int(input())

def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    leftList = list[:mid]
    rightList = list[mid:]
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    return merge(leftList, rightList)

def merge(left, right):
    global cnt
    left_len = len(left)
    right_len = len(right)
    result = [0] * (left_len + right_len)
    i = 0
    left_i = 0
    right_i = 0
    if left[-1] > right[-1]:
        cnt += 1
    while i < (left_len + right_len):
        if left_i < left_len and right_i < right_len:
            if left[left_i] <= right[right_i]:
                result[i] += left[left_i]
                i += 1
                left_i += 1
            else:
                result[i] += right[right_i]
                i += 1
                right_i += 1
        elif left_i < left_len:
            result[i] += left[left_i]
            i += 1
            left_i += 1
        elif right_i < right_len:
            result[i] += right[right_i]
            i += 1
            right_i += 1
    return result

for tc in range(1, T + 1):
    N = int(input())
    jungsu = list(map(int, input().split()))
    L = N//2
    cnt = 0
    result = merge_sort(jungsu)

    dab = result[L]
    print("#%d %d %d" %(tc, dab, cnt))