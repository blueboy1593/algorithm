import sys
sys.stdin=open("A_input.txt", "r")

def move(i):
    atom = atom_list[i]
    if atom[2]==0:
        atom[1] -= 1
    elif atom[2]==1:
        atom[1] += 1
    elif atom[2]==2:
        atom[0] -= 1
    elif atom[2]==3:
        atom[0] += 1


def crush(atom_list):
    tuple_list=[]
    for i in range(len(atom_list)):
        new_tup=[atom_list[i][0], atom_list[i][1]]
        if new_tup in tuple_list:
            address.append(i)
            crush_list.append(new_tup)
        tuple_list.append(new_tup)

    while crush_list != []:
        for i in range(len(tuple_list)):
            if crush_list[-1] == tuple_list[i]:
                address.append(i)
                crush_list.pop()
                break

def del_crush(address):
    if address == []:
        return
    address = sorted(address)


def find_crush(time):
    if time == 2001:
        return
    for i in range(len(atom_list)):
        move(i)
    crush(atom_list)
    del_crush(address)
    find_crush(time + 1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    atom_list = [ list(map(int, input().split())) for _ in range(N) ]
    crush_list=[]
    address=[]
    energy = 0
    # print(atom_list)
    t = 0
    # empty = [ [0]*2001 for _ in range(2001) ]
    find_crush(t)
