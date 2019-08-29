import sys
sys.stdin=open("4875_input.txt", "r")

def is_ok(y, x):    #해당 좌표가 이동가능한지 여부
    return 0<=y<n and 0<=x<n and mymap[y][x] != 1

def find_map(startY, startX):
    global result
    # 1. 종료조건
    if mymap[startY][startX]==3:
        result = 1
        return #검색 종료
    # 2. 반복검색

    visited.append( (startY,startX) )
    # 4방향 검색
    if result==0 and is_ok(startY, startX + 1) and (startY, startX+1) not in visited:
        find_map(startY, startX + 1)
    if result==0 and is_ok(startY + 1, startX) and (startY + 1, startX) not in visited:
        find_map(startY + 1, startX)
    if result==0 and is_ok(startY, startX - 1) and (startY, startX-1) not in visited:
        find_map(startY, startX - 1)
    if result==0 and is_ok(startY - 1, startX) and (startY - 1, startX) not in visited:
        find_map(startY - 1, startX)


TC = int(input())

for tc in range(1, TC+1):
    n = int(input())  # 한변의 길이
    mymap = []  # 지도 정보
    for i in range(n):
        l = list( input() )
        row_list=list(map(int,l))
        mymap.append(row_list)
    # print("mymap", mymap)
    # 시작지점 찾기
    startX = -1
    startY = -1
    for y in range(n):
        for x in range(n):
            if mymap[y][x]== 2:
                startX, startY = x, y
    # 미로 -> 방문했던 위치 저장소
    visited = []
    result = 0  # 목적지 도착 여부
    find_map(startY, startX)
    print(result)