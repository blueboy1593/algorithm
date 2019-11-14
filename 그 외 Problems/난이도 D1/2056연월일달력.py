import sys
sys.stdin=open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    real = True
    num_list = list(map(int, input()))
    month = num_list[4]*10 + num_list[5]
    day = num_list[6]*10 + num_list[-1]
    if month > 12 or month ==0:
        real = False

    if (month == 4 or month == 6 or month == 9 or month == 11) and (day == 0 or day > 30):
        real = False
    elif month == 2 and (day ==0 or day > 28):
        real = False
    else:
        if day==0 or day > 31:
            real = False
    if month < 10:
        month = '0' + str(month)
    else:    
        month = str(month)

    if day < 10:
        day = '0' + str(day)
    else:
        day = str(day)
    
    year = ''.join(map(str,num_list[:4]))

    if real == True:
        print("#%d %s/%s/%s" %(tc, year, month, day))
    else:
        print("#%d -1" %tc)