print(__name__)

# n = 3 + 2 + 1

def mysum(num):
    # 멈춤조건
    if num == 1:
        return 1
    return num + mysum(num-1)

n = mysum(5)
print(n)
