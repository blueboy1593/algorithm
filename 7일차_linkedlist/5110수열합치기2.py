import sys
sys.stdin = open("5110_input.txt", "r")

T = int(input())

class Node:
    def __init__(self, data, link = None):
        self.data = data
        self.link = link

    def addtoFirst(data):
        global Head
        Head = Node(data, Head)

    def add(pre, data):
        if pre == None:
            print('error')
        else:
            pre.link = Node(data, pre.link)

    def addtoLast(data):
        global Head
        if Head == None:
            Head = Node(data, None)
        else:
            p = Head
            while p.link != None:
                p = p.link
            p.link = Node(data, None)

    def __str__(self):  # 객체의 내부정보를 문자열로 반환
        return "data=%s, link=%s" %(self.data, self.link)
    def __repr__(self): # JSON 문자열로 반환. 추후 JSON.parse()로 복구 위한 문자열
        return "data:%s, link:%s" %(self.data, self.link)

a = [1,2,3]
b = [3,4,5]
c = [5,6,7]

aa = Node(a)
bb = Node(b)
print(aa)
aa.addtoLast(bb)
print(aa)


# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     suyeol = []
#     push = False
#     for _ in range(M):
#         temp = list(map(int, input().split()))
#         suyeol.append(temp)