from itertools import combinations

def solution(numbers):
    answer = []
    for combo in combinations(numbers, 2):
        answer.append(sum(combo))
    #중복제거
    answer_set = set(answer)
    answer_list = list(answer_set)
    #오름차순
    answer_list.sort()
    return answer_list