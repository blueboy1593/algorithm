N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = 0
for i in range(N):
    A[i] -= B
    cnt += 1
    if A[i] <= 0:
        continue
    else:
        if A[i] % C == 0:
            temp_cnt = A[i]//C
        else:
            temp_cnt = A[i]//C + 1
        cnt += temp_cnt

print(cnt)