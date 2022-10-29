from collections import deque
n,m=map(int,input().split())
bank=n
queue=deque()
def deposit(price):
    global bank
    bank+=price
    if queue and queue[0]<=bank:
        bank-=queue.popleft()
def reservation(price):
    global bank
    if bank<price:
        queue.append(price)
    else:
        if queue:
            queue.append(price)
        elif bank>=price:
          bank-=price
def pay(price):
    global bank
    if bank>=price:
        bank-=price
for _ in range(m):
    category,price=map(str,input().split())
    price=int(price)
    if category=="deposit":
        deposit(price)
    elif category=="pay":
        pay(price)
    else:
        reservation(price)
print(bank)