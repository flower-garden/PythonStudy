a=[[1, 4], [9, 2], [3, 8], [11, 6]]
b=[[3, 5], [4, 1], [2, 4], [5, 10]]
#x=[a,b,c,d] 조합 => [a,b],[a,c],[a,d],[b,c]
#평행 조건 : 기울기가 같고, y절편이 다름
#기울기 공식 : (y2-y1) / (x2-x1) = m
#y절편 : 기울기a 일 때 -> y=m(x-x1)+y1 -> y절편 = y1-mx1

#조합 생성
def make_comb(a,b,arr):
  com=[]
  for i in range(a,b):
    for j in range(a,b):
      if i+j+1>b:
        continue
      com.append((arr[i],arr[i+j+1]))
  return com

#순차 탐
def seq_serch(a,b,arr):
  for i in range(a,b):
    for j in range(a,b):
      if i+j+1>b:
        continue
      elif arr[i]==arr[i+j+1]:
        return 1
  return 0

def solution(dots):
  com=make_comb(0,3,dots)
  m=[]
  for i in com:
    m.append(float((i[0][1]-i[1][1])/(i[0][0]-i[1][0])))
  return seq_serch(0,5,m)

print(f"a:{solution(a)}\nb:{solution(b)}")