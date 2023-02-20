def solution(book_time):
    answer = 1  #room
    lis = []  #

    for i, j in enumerate(book_time):
        #시간 수치화
        book_time[i] = [
            int(j[0][:2]) * 60 + int(j[0][3:]),
            int(j[1][:2]) * 60 + int(j[1][3:]) + 10
        ]
    book_time.sort()

    for i, j in book_time:
        if not lis:
            lis.append(j)
            continue

        if lis[0] <= i:
            lis.pop(0)  #지난 룸 시간 제외

        else:
            answer += 1

        lis.append(j)  #예약 종료시간 끝에 추추가
        lis.sort()  #예약 종료시간 오름차순
    return answer


time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"],
        ["14:10", "19:20"], ["18:20", "21:20"]]

print(solution(time))
