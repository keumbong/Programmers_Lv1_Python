def solution(scores):
    rank, avg = [], []
    re_sco = [[0] * len(scores) for _ in range(len(scores))]

    # 행렬 재정렬 (행과 열을 바꿈)
    for i in range(len(scores)):
        for j in range(len(scores)):
            re_sco[i][j] = scores[j][i]

    # 자기 자신에게 유일한 최고점, 최저점 제거
    for i in range(len(scores)):
        if (re_sco[i][i] == max(re_sco[i]) and re_sco[i].count(max(re_sco[i])) == 1) or (
                re_sco[i][i] == min(re_sco[i]) and re_sco[i].count(min(re_sco[i])) == 1):
            del re_sco[i][i]

    # 평균 구하기
    for i in re_sco:
        avg.append(sum(i) / len(i))
    for i in avg:
        if i >= 90:
            rank.append('A')
        elif i >= 80 and i < 90:
            rank.append('B')
        elif i >= 70 and i < 80:
            rank.append('C')
        elif i >= 50 and i < 70:
            rank.append('D')
        else:
            rank.append('F')
    return ''.join(rank)