import sys
sys.stdin=open("sample_input.txt", "r")

T=int(input())

for tc in range(1, T+1):
    first=input()
    second=input()

    my_dict = {}
    for fir in first:
        my_dict[fir] = 0
    
    for sec in second:
        if sec in my_dict.keys():
            my_dict[sec] += 1
    
    alist=list(my_dict.values())
    maxa = max(alist)
    print("#%d %d" %(tc, maxa))