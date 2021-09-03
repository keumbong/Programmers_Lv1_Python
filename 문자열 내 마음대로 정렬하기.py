def solution(strings, n):
    answer = []
    for i in strings:
        answer.append(i[n] + i)  # 문자열 앞에 n번째 인자 붙이기
    answer.sort()

    return [j[1:] for j in answer]