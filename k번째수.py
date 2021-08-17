def solution(array, commands):
    answer = []

    for arr in commands:
        i, j, k = arr[0], arr[1], arr[2]
        array_re = array[i - 1:j]
        array_re.sort()
        answer.append(array_re[k - 1])

    return answer