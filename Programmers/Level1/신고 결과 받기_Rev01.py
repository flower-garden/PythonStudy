#23.02.21 개선
def solution(id_list, report, k):
  answer = [0]* len(id_list)
  dic_num={x:0 for x in id_list}
  set_report=set(report)
  
  for i in set_report:
    dic_num[(i.split())[1]]+=1
    
  for i,j in enumerate(set_report):
    lis=j.split()
    if dic_num[lis[1]]>=k:
      answer[id_list.index(lis[0])]+=1
  
  return answer

id_list=["muzi", "frodo", "apeach", "neo"]
report=["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi", "muzi frodo"]
k=2

print(solution(id_list, report, k))
#result [2,1,1,0]