import sys
sys.stdin=open("4881_input.txt", "r")

def find_min(row):
    global submin, mymin

    #if submin > mymin: #누적중인값이 최소값보다 크면 하위검색 중단
        #return 여기는 부가적인 옵션.
    if row == n: #맨 아래까지 내려왔으면
        if submin < mymin: #누적값이 최소값보다 작으면 최소값 갱신
            mymin = submin
        return # 더이상 내려가지 않음.

    for x in range(n):
        if visited[x]==0: # 각 함수마다 적용이 다르게 되나보다.
            visited[x] = 1
            submin += mymap[row][x] # 최소값 누적변수에 누적
            find_min(row+1)
            visited[x] = 0
            submin -= mymap[row][x] # 들어갔다가 나왔으니 누적숫자만큼 뺌

TC = int(input())
for tc in range(1, TC+1):
    n = int(input()) # 한변의 길이
    mymap = [list(map(int, input().split()))for i in range(n)]
    visited = [0]*n #n개의 0을 가지는 배열
    mymin = 99999999  #최소값 저장용
    submin = 0  #중간 열별 값 저장용. 최소값보다 작으면 최소값에 저장.
    find_min(0)
    print("#%d %d" %(tc, mymin))