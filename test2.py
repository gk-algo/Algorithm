import heapq
def getResult(standard,discount, emoticions):
    price=0
    for emoticion in emoticions:
        emoticionPrice=emoticion-(emoticion/100*discount)
        if price+emoticionPrice<standard:
            price+=int(emoticionPrice)
        else:
            return True
    print(price)
    return price

def solution(users, emoticons):
    answers = []
    discounts=[]
    for discount, standard in users:
        heapq.heappush(discounts,discount)
    while discounts:
        answer=[0,0]
        thiscount=heapq.heappop(discounts)
        for userDiscount, userStandard in users:
            print(userDiscount,thiscount)
            if userDiscount<=thiscount:
                result=getResult(userStandard, thiscount, emoticons)
                if result==True:
                    answer[0]+=1
                else:
                    answer[1]+=result
        answers.append(answer)
    return answers
print(solution([[40, 10000], [25, 10000]],[7000, 9000]))