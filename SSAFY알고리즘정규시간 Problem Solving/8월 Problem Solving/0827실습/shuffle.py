import sys
sys.stdin=open("ad_input.txt", "r")

# def x1(card, N):
#     half = N/2
#     card[half-1], card[half] = card[half], card[half-1]
#     return card
#
# def x2(card, N):
#     nlist = []
#     h = N/2
#     for i in range(h):
#         nlist.append(card[i])
#         nlist.append(card[h+i])
#     return nlist
#
# def x3(card, N):
#     nlist = []
#     h = N/2
#     for i in range(h):
#         nlist.append(card[h + i])
#         nlist.append(card[i])
#     return nlist
#
# def x4(card, N):
#     nlist=[]
#     h = N/2
#     for i in range(h):
#         nlist.append(card[h + i])
#     for i in range(h):
#         nlist.append(card[i])
#     nlist[h-1], nlist[h] = nlist[h], nlist[h-1]
#     return nlist
#
# def x5(card, N):
#     nlist=[]
#     h = N/2
#     for i in range(h):
#         nlist.append(card[h + i])
#     for i in range(h):
#         nlist.append(card[i])
#     return nlist

def shuffle(card, i, N):
    nlist=[]
    h = int(N/2)
    kim = h - i
    help = h - kim
    if N == 2:
        return card
    else:
        if i <= h-1:
            for m in range(kim):
                nlist.append(card[m])
            for m in range(help):
                nlist.append(card[h + m])
                nlist.append(card[h-i+m])
            for m in range(kim):
                nlist.append(card[h+i+m])
        # elif i == h-1:
        #     for m in range(h):
        #         nlist.append(card[m])
        #         nlist.append(card[m+h])
        # elif i == h:
        #     for m in range(h):
        #         nlist.append(card[m+h])
        #         nlist.append(card[m])
        else:
            kim = i - h + 1
            help = h - kim
            for m in range(kim):
                nlist.append(card[h+m])
            for m in range(help):
                nlist.append(card[m])
                nlist.append(card[h+1+m])
            for m in range(kim):
                nlist.append(card[h-1+m])
        return nlist

def docheck(card, n, N):
    if n == 5:
        return -1
    else:
        for i in range(1, N):
            a = shuffle(card, i, N)
            n += 1
            if ifdab(a)==True:
                return n
            else:
                docheck(a, n, N)

def ifdab(card):
    global orem_list
    global naelim_list
    if card == orem_list or card == naelim_list:
        return True

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card_list = list(map(int, input().split()))
    orem_list = sorted(card_list)
    naelim_list = orem_list[::-1]
    n = 0
    result = 0
    # if ifdab(card_list)==True:
    #     result = 1

    # print(result)
    print(card_list)
    bb = shuffle(card_list, 3, N)
    print(bb)
    # docheck(card_list, n, N)

    # print(orem_list)
    # print(naelim_list)
