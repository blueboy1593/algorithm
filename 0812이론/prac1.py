al = 'Reverse the strings'
al = list(al)
for i in range(len(al)//2):
    al[i], al[-1-i] = al[-1-i], al[i]


# al = map(str, al)
al = ''.join(al)
print(al)