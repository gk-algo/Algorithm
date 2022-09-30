def add_date(pday, category,termsDic):
    year,month,day=map(int, pday.split("."))
    if month+termsDic[category]>12:
        year+=1
        month=month+termsDic[category]-12
    else:
        month=month+termsDic[category]
    if day==1:
        month=month-1
        day=28
    else:
        day-=1
    year=str(year)
    month=str(month)
    day=str(day)
    if len(month)<2:
        month='0'+month
    if len(day)<2:
        day='0'+day
    return int(year+month+day)

def solution(today, terms, privacies):
    answer = []
    year, month, day=today.split('.')
    today=int(year+month+day)
    termsDic={}
    dates=[]
    for term in terms:
        category,duration=term.split(" ")
        termsDic[category]=int(duration)
    for privacy in privacies:
        pday,category=privacy.split(" ")
        dates.append(add_date(pday,category,termsDic))
    for i in range(len(dates)):
        print(dates[i], today)
        print(dates[i]<today)
        if dates[i]<today:
            answer.append(i+1)
    return answer
print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01",["Z 3", "D 5"],["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))