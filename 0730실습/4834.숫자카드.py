N = int(input())

for i in range(1, N+1):
    card_jang = int(input())
    card = list(map(int, input()))
    count_max = sorted(card).count(0)
    for card_num in sorted(card):
        if card.count(card_num) >= count_max:
            count_max = card.count(card_num)
            max_card = card_num
    
    print('#%d %d %d' %(i,max_card,count_max))
