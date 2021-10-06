def solution(numbers):
    arr = [i for i in range(10)]
    answer = [i for i in arr if i not in numbers]
    return sum(answer)