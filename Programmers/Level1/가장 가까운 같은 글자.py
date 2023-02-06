def solution(s):
  answer = []
  dic={}
  for i,v in enumerate(s):
    answer.append(-1) if v not in dic else answer.append(i-dic[v])
    dic[v]=i
    
  return answer

s="foobar"
print(solution(s))