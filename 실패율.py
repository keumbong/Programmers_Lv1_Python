def solution(N, stages):
    answer = {}
    n = len(stages)

    for stage in range(1, N + 1):
        if n != 0:
            answer[stage] = stages.count(stage) / n
            n -= stages.count(stage)
        else:
            answer[stage] = 0
    return sorted(answer, key=lambda x: answer[x], reverse=True)