for i in range(1,11):
    dump = int(input())
    hite = list(map(int, input().split()))

    for j in range(dump):
        for k in range(len(hite)):
            if hite[k] == max(hite):
                hite[k] -= 1
                break
        for k in range(len(hite)):
            if hite[k] == min(hite):
                hite[k] += 1
                break
    pyeongtanhwa = max(hite) - min(hite)
    print('#%d %d' %(i,pyeongtanhwa))