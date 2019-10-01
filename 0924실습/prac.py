TF = [False] * 10
# for i in range(10):
#     if i % 3 == 1:
#         TF[i] = True
print(TF)

def prac(i, TF):
    print(TF)
    if i == 9:
        return
    for j in range(1, 6):
        if i + j < 10:
            
            TF[i + j] = True
            prac(i + j, TF)

prac(0, TF)