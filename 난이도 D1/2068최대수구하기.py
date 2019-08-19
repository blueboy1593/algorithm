import sys
sys.stdin=open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    num_list = list(map(int, input().split()))
    num_max=0
    for num in num_list:
        if num > num_max:
            num_max = num

    print('#%d %d' %(tc, num_max))