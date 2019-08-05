import random

my_list = list(range(26))
random.shuffle(my_list)
arr = []

for i in range(5):
    temp_list = []
    for j in range(5):
        temp_list.append(my_list[i*5+j])
    arr.append(list(temp_list))

arr = [[1,1,1,1,1],
       [1,0,0,0,1],
       [1,0,0,0,1],
       [1,0,0,0,1],
       [1,1,1,1,1]]
# arr = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25]]

abs_sum = 0
for i in range(5):
    for j in range(5):
        # 왼쪽 처리
        if i == 0:
            # abs_sum += arr[0][j]
            pass
        else:
            abs_sum += abs(arr[i][j] - arr[i-1][j])
        # 오른쪽 처리
        if i == 4:
            # abs_sum += arr[4][j]
            pass
        else:
            abs_sum += abs(arr[i][j] - arr[i+1][j])  
        # 위쪽 처리
        if j == 0:
            # abs_sum += arr[i][0]
            pass
        else:
            abs_sum += abs(arr[i][j] - arr[i][j-1]) 
        # 아래쪽 처리
        if j == 4:
            # abs_sum += arr[i][4]
            pass
        else:
            abs_sum += abs(arr[i][j] - arr[i][j+1]) 

print(arr)
print(abs_sum)