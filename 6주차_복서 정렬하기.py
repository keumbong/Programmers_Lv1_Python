def solution(weights, head2head):
    answer = []
    for i in range(len(head2head)):
        win, cnt, win_big = 0, 0, 0
        for j in range(len(head2head)):
            if head2head[i][j] == 'W' or head2head[i][j] == 'L':
                cnt += 1
                if head2head[i][j] == 'W':
                    win += 1
                    if weights[i] < weights[j]:
                        win_big += 1
        if cnt == 0:
            win_rate = 0
        else:
            win_rate = (win / cnt) * 100
        answer.append((i + 1, win_rate, win_big, weights[i]))

    arr = sorted(answer, key=lambda x: (-x[1], -x[2], -x[3], x[0]))

    result = [i[0] for i in arr]
    return result