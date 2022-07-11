t = int(input())
for _ in range(t) :
    n = int(input())
    num = [1 for x in range(10)]
    for _ in range(1,n) :
        n=num[:]
        num[0] = n[7]
        num[1] = n[2] + n[4]
        num[2] = n[1] + n[3] + n[5]
        num[3] = n[2] + n[6]
        num[4] = n[1] + n[5] + n[7]
        num[5] = n[2] + n[4] + n[6] + n[8]
        num[6] = n[3] + n[5] + n[9]
        num[7] = n[4] + n[8] + n[0]
        num[8] = n[5] + n[7] + n[9]
        num[9] = n[6] + n[8]

    print(sum(num)%1234567)