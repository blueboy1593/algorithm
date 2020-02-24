import sys
sys.stdin=open("input.txt", "r")

T = int(input())
num_list = list(map(int, input().split()))

sorlist = sorted(num_list)
mid_num = sorlist[len(sorlist)//2]

print('%d' %(mid_num))