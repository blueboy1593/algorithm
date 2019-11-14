import sys
sys.stdin=open("1267_input.txt", "r")

TC = 10
for tc in range(1, TC+1):
    mynode, myline = map(int, input().split()) # 노드 수, 간선 수
    mymap = [ [0]*(mynode+1) for i in range(mynode+1) ] # 2차원 맵 생성
    # 간선정보 입력
    data = list(map(int, input().split()))
    n = int(len(data)/2)    # 나누기 결과는 실수 -> 정수로 변환

    for i in range(n):
        start = data[i*2]
        end = data[i*2 + 1]
        mymap[end][start] = 1 # 이인동

    result=[]
    while True:
        if len(result) == mynode:   #전체 노드가 경로에 모두 저장되면 검색 중단
            break
        start_col = []
        for col in range(1, len(mymap)):   # 모든 칼럼을 검색
            if 1 not in mymap[col] and col not in result:   # 작업경로에 등록 안된
                start_col.append(col)
        for col in start_col:
            result.append(col)  # 작업경로에 등록
            for row in range(len(mymap)):
                mymap[row][col]=0   # 출발하는 노드로 연결되는 정보 삭제

    print("#%d" %tc, end=" ")
    for i in result:
        print("%d"%i, end=" ")
    print()