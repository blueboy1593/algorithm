munza=list(input())

def itoa(word):
    for i in range(len(word)):
        try:
            if int(word[i]):
                word[i]=int(word[i])
        except ValueError:
            pass

    print(word)


itoa(munza)
