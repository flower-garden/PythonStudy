'''
23.02.05 개선 필요
1.문제를 잘 읽어야함 : 모든 달은 28일로 한다고 기술되어 있음
2.달마다 일수를 곱해서 값을 비교하는것도 좋음
'''


def solution(today, terms, privacies):
    answer = []
    spl_today = list(map(int, today.split('.')))  #today split list
    dic_terms = {}  #terms dictionary
    spl_priv = []  #privacies split list

    for i in terms:  #dic_terms define
        div = i.split()
        dic_terms[div[0]] = int(div[1])

    for i in privacies:  #spl_priv define : int and str
        i = i.replace('.', ' ')
        i = i.split()
        st = i[3]
        i = list(map(int, i[:3]))
        i.append(st)
        spl_priv.append(i)

    num = 1
    for i in spl_priv:
        x_mon = dic_terms[i[3]] + i[1]
        if x_mon % 12 != 0:
            com = [i[0] + (x_mon // 12), x_mon % 12, i[2] -
                   1] if x_mon > 12 else [i[0], x_mon, i[2] - 1]
        else:
            com = [i[0] + (x_mon // 12) - 1, x_mon % 12 + 12, i[2] -
                   1] if x_mon > 12 else [i[0], x_mon, i[2] - 1]

        if com[2] == 0:
            ## 31day not 2,4,6,9,11
            if com[1] == 2 or com[1] == 4 or com[1] == 6 or com[1] == 9 or com[
                    1] == 11:
                com[2] = 31
            elif com[1] == 3:
                com[2] = 29 if ((com[0] % 4 == 0) and
                                (com[0] % 100 != 0)) or (com[0] %
                                                         400 == 0) else 28
            else:
                com[2] = 30
            com[1] -= 1
        print(com)

        if spl_today[0] == com[0]:
            if spl_today[1] < com[1]:
                num += 1
                continue
            elif spl_today[1] > com[1]:
                answer.append(num)
                num += 1
                continue
            else:
                if spl_today[2] > com[2]:
                    answer.append(num)
                    num += 1
                    continue
                else:
                    num += 1
                    continue

        elif spl_today[0] < com[0]:
            num += 1
            continue
        else:
            answer.append(num)
            num += 1

    return answer


terms = ["B 12"]
privacies = ["2017.12.21 B"]
today = "2019.01.01"

print(solution(today, terms, privacies))
