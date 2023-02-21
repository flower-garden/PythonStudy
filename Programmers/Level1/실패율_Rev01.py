'''
# 실패율 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
#전체 스테이지 개수 N / 사용자가 현재 멈춰있는 스테이지 번호가 담긴 배열 stages
#실패율이 높은 스테이지부터 내림차순으로 스테이지 번호가 담겨있는 배열 return
def failure():
    
스테이지의 개수 N은 1 이상 500 이하의 자연수이다.
stages의 길이는 1 이상 200,000 이하이다.
stages에는 1 이상 N + 1 이하의 자연수가 담겨있다.
각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.
단, N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자를 나타낸다.
만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.

N	stages	result
5	[2, 1, 2, 6, 2, 4, 3, 3]	[3,4,2,1,5]
4	[4,4,4,4,4]	[4,1,2,3]

입출력 예 #1
1번 스테이지에는 총 8명의 사용자가 도전했으며, 이 중 1명의 사용자가 아직 클리어하지 못했다. 따라서 1번 스테이지의 실패율은 다음과 같다.

1 번 스테이지 실패율 : 1/8
2번 스테이지에는 총 7명의 사용자가 도전했으며, 이 중 3명의 사용자가 아직 클리어하지 못했다. 따라서 2번 스테이지의 실패율은 다음과 같다.

2 번 스테이지 실패율 : 3/7
마찬가지로 나머지 스테이지의 실패율은 다음과 같다.

3 번 스테이지 실패율 : 2/4
4번 스테이지 실패율 : 1/2
5번 스테이지 실패율 : 0/1
각 스테이지의 번호를 실패율의 내림차순으로 정렬하면 다음과 같다.

[3,4,2,1,5]
입출력 예 #2

모든 사용자가 마지막 스테이지에 있으므로 4번 스테이지의 실패율은 1이며 나머지 스테이지의 실패율은 0이다.

[4,1,2,3]
'''


#23.02.01 시간복잡도 개선 Version
def failure(N, stages):
	stage_user = [0] * (N + 1)  #스테이지 별 실패자
	stage_user_sum = []  #스테이지 별 도전자
	stage_failure = {}  #스테이지 별 실패율
	
	for i in stages:
		stage_user[i - 1] += 1
	print(stage_user)

	for i in range(N):
		stage_user_sum.append(sum(stage_user[i:N + 1]))
	print(stage_user_sum)

	for i in range(0, N):
		if (stage_user_sum[i]):
			stage_failure[i + 1] = stage_user[i] / stage_user_sum[i]
		else:
			stage_failure[i + 1] = 0
	return stage_failure


def solution(N, stages):
	dic = dict(sorted(failure(N, stages).items(), key=lambda x: x[1], reverse=True))
	print(dic)
	answer = list(dic.keys())
	return answer


N = 5
stage = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stage))
