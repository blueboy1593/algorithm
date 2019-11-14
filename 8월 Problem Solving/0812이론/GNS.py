import sys
sys.stdin=open("input.txt", "r")

T=int(input())

for tc in range(1, T+1):
    tc_num = str(input())
    num_list = list(map(str, input().split()))
    result_list = []

    for num in num_list:
        if num == 'ZRO':
            result_list.append('ZRO')
    for num in num_list:
        if num == 'ONE':
            result_list.append('ONE')
    for num in num_list:
        if num == 'TWO':
            result_list.append('TWO')
    for num in num_list:
        if num == 'THR':
            result_list.append('THR')
    for num in num_list:
        if num == 'FOR':
            result_list.append('FOR')
    for num in num_list:
        if num == 'FIV':
            result_list.append('FIV')
    for num in num_list:
        if num == 'SIX':
            result_list.append('SIX')
    for num in num_list:
        if num == 'SVN':
            result_list.append('SVN')
    for num in num_list:
        if num == 'EGT':
            result_list.append('EGT')
    for num in num_list:
        if num == 'NIN':
            result_list.append('NIN')

    result = ' '.join(result_list)
    print('#%d' %tc)
    print(result)
