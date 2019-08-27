def quickSort(a, begin, end):
    if begin < end:
        p = partition(a, begin, end)
        quickSort(a, begin, p-1)
        quickSort(a, P+1, end)

def partition(a, begin, end):
    pivot = (begin + end)//2
    L = begin
    R = end
    while L < R:
        while(a[L]<a[pivot] and L<R) : L += 1
        while(a[R]>=a[pivot] and L<R) : R -= 1
        if L < R:
            if L==pivot: pivot = R
            a[L], a[R] = a[R], a[L]
    a[pivot], a[R] = a[R], a[pivot]
    return R

alist = [10, 20, 35, 40, 5, 23, 80, 100, 55, 60]
quickSort(alist)