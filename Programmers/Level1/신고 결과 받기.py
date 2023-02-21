#23.02.21 개선 필요
def solution(id_list, report, k):
  answer = [0]* len(id_list)
  dic_num={x:0 for x in id_list}
  re_list=[x.split() for x in report]
  dic_user={x:[] for x in id_list}

  for i,j in re_list: #유저 당 신고한 ID
    dic_user[i].append(j)
  for i in  dic_user:
    dic_user[i]=set(dic_user[i])
  for i in dic_user:
    for j in set(dic_user[i]):
      dic_num[j]+=1

  for x,y in enumerate(dic_user.values()):
    for i in y:
      if dic_num[i]>=k:
        answer[x]+=1
  
  return answer

id_list=["muzi", "frodo", "apeach", "neo"]
report=["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi", "muzi frodo"]
k=2

print(solution(id_list, report, k))
#result [2,1,1,0]