import sys
sys.stdin=open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    num_list = list(map(int, input().split()))
    sum = 0
    for num in num_list:
        sum += num
    aver = sum/10
    aver = round(aver)
    
    print('#%d %d' %(tc, aver))