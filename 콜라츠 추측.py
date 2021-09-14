def solution(num):
    answer = (-1)
    cnt = 0
    while num != 1:
        if num % 2 == 0:
            num /= 2
            cnt += 1
        elif num % 2 == 1:
            num = (num*3) + 1
            cnt += 1
    return cnt if cnt < 500 else answer