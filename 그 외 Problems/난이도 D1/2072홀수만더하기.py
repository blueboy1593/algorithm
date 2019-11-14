import sys
sys.stdin=open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    num_list = list(map(int, input().split()))
    sum = 0
    for num in num_list:
        if num%2==1:
            sum += num
    print('#%d %d' %(tc, sum))