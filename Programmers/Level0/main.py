'''
for i in range(1,11):
    print(' '*(10-i), end='')
    print('*'*(2*i-1), end='')
    print()
'''
#Test Case
a=["ayaaya", "yee", "u", "maa", "wyeoo"]
b=["ayayeq", "woouuuma", "zzye", "ayayemawooaya", "ayaa"]

def solution(babbling):
  answer=0
  com=0 #Comparison
  words=["aya", "ye", "woo", "ma"]
  
  for i in babbling:
    a=i #Test Case 안에 발음 불가능한 words가 있는가
    
    for j in words:
      if(j in i and a in i): #babbling 속에 words가 있고, a가 기존 babbling에 속하는가
        com+=1
        #babbling 속에 발음 가능한 words가 있으면 제거하여서 최종적으로 발음 가능한 str인지 아닌지
        a=a.replace(j,'',1) 
        
      #a==''인 경우는 모두 발음 가능한 babbling이였고, not in 이면 발음 불가능이기 때문에 탈출
      if(a=='' or a not in i): 
        break

    #발음 불가능한 str일 때, 초기화
    if(a!=''):
      com=0
      continue
    answer=com if com>answer else answer
    com=0
  return answer

print(f"a:{solution(a)}\nb:{solution(b)}")