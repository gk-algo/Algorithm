from collections import deque
n,m=map(int,input().split())
bank=n
queue=deque()
def deposit(bank,price):
    bank+=price
    while queue and queue[0]<=bank:
        bank-=queue.popleft()
    return bank

def reservation(bank,price):
    if not queue and price<=bank:
        bank-=price
    else:
        queue.append(price)
    return bank

def pay(bank,price):
    if bank>=price:
        bank-=price
    return bank

for _ in range(m):
    category,price=map(str,input().split())
    price=int(price)
    
    if category=="deposit":
        bank=deposit(bank,price)
    elif category=="pay":
        bank=pay(bank,price)
    elif category=="reservation":
        bank=reservation(bank,price)
print(bank)