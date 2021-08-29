def solution(n):
    n_re = list(str(n))
    n_re.sort(reverse=True)
    answer = "".join(n_re)

    return int(answer)