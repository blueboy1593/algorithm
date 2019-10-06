N = int(input())

# rope = []
# for _ in range(N):
#     rope.append(int(input()))

rope = [0] * N
for i in range(N):
    rope[i] = int(input())
rope.sort()
maxmax = 0

for batjul in rope:
    temp = batjul * N
    if temp > maxmax:
        maxmax = temp
    N -= 1

print(maxmax)