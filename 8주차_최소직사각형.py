def solution(sizes):
    tmp = 0
    for a in sizes:
        if a[0] < a[1]:
            a[0], a[1] = a[1], a[0]
    sizes.sort(key = lambda x : -x[0])
    max_x = sizes[0][0]
    sizes.sort(key = lambda x : -x[1])
    max_y = sizes[0][1]
    return max_x * max_y