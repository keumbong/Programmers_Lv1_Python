def solution(lottos, win_nums):
    answer = []
    rank = [6, 6, 5, 4, 3, 2, 1]
    cnt = 0
    cntz = lottos.count(0)  # 0의 개수 카운트

    for i in lottos:
        if i in win_nums:
            cnt += 1
    answer.append(rank[cnt + cntz])
    answer.append(rank[cnt])
    return answer