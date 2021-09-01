def solution(n):
    answer = 0
    number = [False, False] + [True] * (n - 1)
    for i in range(2, n + 1):
        if number[i] == True:
            for j in range(i * 2, n + 1, i):
                number[j] = False
    for k in range(2, n + 1):
        if number[k] == True:
            answer += 1

    return answer