def solution(a, b):
    answer, tmp = 0, 0
    if a > b:
        tmp = a
        a = b
        b = tmp
    for i in range(a, b + 1):
        if a == b:
            return a
        answer += i
    return answer