def solution(n):
    answer, result = 0, 0
    my_list = []
    if n < 3:
        return n
    else:
        while True:
            answer = divmod(n, 3)
            n = answer[0]
            my_list.append(answer[1])
            if n < 3:
                my_list.append(answer[0])
                break
    for i in range(len(my_list)):
        result += 3**(len(my_list) - 1 - i) * (my_list[i])
    return result