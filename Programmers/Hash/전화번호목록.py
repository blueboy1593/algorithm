def solution(phone_book):
    answer = True
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if i != j:
                if len(phone_book[i]) > len(phone_book[j]):
                    continue
                flag = True
                for k in range(len(phone_book[i])):
                    if phone_book[i][k] != phone_book[j][k]:
                        flag = False
                        break
                if flag == True:
                    return False
    return answer