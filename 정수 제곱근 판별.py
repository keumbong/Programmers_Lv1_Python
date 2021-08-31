import math
def solution(n):
    answer = math.sqrt(n)
    if answer % 1 == 0:
        result = pow(answer+1,2)
    else:
        result = -1
    return result