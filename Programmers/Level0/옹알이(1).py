#Test Case
a=["ayaaya", "yee", "u", "maa", "wyeoo"]
b=["ayayeq", "woouuuma", "zzye", "ayayemawoo", "ayaa"]

def solution(babbling):
  answer=0
  words=["aya", "ye", "woo", "ma"]
  
  for i in babbling:
    for j in words:
      #babbling 속에 words가 있으면 최대 1번만 ^로 변경
      #''으로 변경할 시, 변경 후 이어지는 단어가 생길 수 있음 ex. mwooa -> ma
      if(j in i):
        i=i.replace(j,'^',1)
    #^으로 치환한 내용을 다시 '' 바꿀 시 i가 ''이면 +1
    if(not i.replace('^','')):
      answer+=1
  return answer

print(f"a:{solution(a)}\nb:{solution(b)}")