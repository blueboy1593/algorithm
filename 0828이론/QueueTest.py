
myque = []

def enQueue(item):
    myque.append(item)
def deQueue():
    return myque.pop(0)

print("myque", myque)
enQueue(100)
enQueue(200)
enQueue(300)
print("myque", myque)
print("deQueue", deQueue())
print("deQueue", deQueue())
print("deQueue", deQueue())
print("myque", myque)
print("OK")