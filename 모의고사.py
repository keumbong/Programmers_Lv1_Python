def solution(answers):
    stu_1 = [1, 2, 3, 4, 5]
    stu_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    stu_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt = [0, 0, 0]
    winner = []
    for i in range(len(answers)):
        if answers[i] == stu_1[i % 5]:
            cnt[0] += 1
        if answers[i] == stu_2[i % 8]:
            cnt[1] += 1
        if answers[i] == stu_3[i % 10]:
            cnt[2] += 1

    for i in range(3):
        if cnt[i] == max(cnt):
            winner.append(i + 1)

    return winner