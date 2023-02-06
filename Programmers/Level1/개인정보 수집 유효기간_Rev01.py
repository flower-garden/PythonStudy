#23.02.06 알고리즘 개선
def solution(today, terms, privacies):
  answer = []
  date_cal=lambda year,month,date: (year*12*28)+(month*28)+date
  spl_today=list(map(int,today.split('.'))) #today split list
  dic_terms = {} #terms dictionary
  spl_priv = [] #privacies split list
    
  for i in terms: #dic_terms define
    div = i.split()
    dic_terms[div[0]] = int(div[1])
    
  for i in privacies: #spl_priv define : int and str
    i = i.replace('.', ' ')
    i = i.split()
    st = i[3]
    i = list(map(int,i[:3]))
    i.append(st)
    spl_priv.append(i)
    
  today_cal=date_cal(spl_today[0],spl_today[1],spl_today[2])
  
  num=1
  for i in spl_priv:
    com=date_cal(i[0],i[1],i[2]-1)+dic_terms[i[3]]*28
    if today_cal > com:
      answer.append(num)
      num+=1
      continue
    else:
      num+=1
      
  return answer


terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"] #2017*(12*28)+12*28+21
today = "2022.05.19" #2019*(12*28)+01*28+01

print(solution(today,terms,privacies))
