list_list = []
for j in range(10):
    n = int(input())
    a_list = list(map(int, input().split()))
    list_list.append(a_list)

def viewjoa(a_list):
    viewcount = 0
    for i in range(2, len(a_list) -1):
        if a_list[i] > a_list[i - 1] and a_list[i] > a_list[i - 2] and a_list[i] > a_list[i + 1] and a_list[i] > a_list[i + 2]:
            view = a_list[i] - max(a_list[i - 1], a_list[i - 2], a_list[i + 1], a_list[i + 2])
            viewcount += view

    return viewcount

bcnt = 1
for b_list in list_list:
    print('#'+ str(bcnt),viewjoa(b_list))
    bcnt += 1