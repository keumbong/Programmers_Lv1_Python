def solution(nums):
    cho = len(nums)/2
    cho = int(cho) #N을 구함
    set_a = set(nums)
    set_list = list(set_a) #중복없는 리스트

    if len(set_list) >= cho:
        answer = cho
    else:
        answer = len(set_list)

    return answer