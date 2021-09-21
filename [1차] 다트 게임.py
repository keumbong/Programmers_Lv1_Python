def solution(dartResult):
    cal = []
    num = ''
    for i in dartResult:
        if i.isdigit():
            num += i
        elif i == 'S':
            num = int(num) ** 1
            cal.append(num)
            num = ''
        elif i == 'D':
            num = int(num) ** 2
            cal.append(num)
            num = ''
        elif i == 'T':
            num = int(num) ** 3
            cal.append(num)
            num = ''
        elif i == '*':
            if len(cal) > 1:
                cal[-2] *= 2
                cal[-1] *= 2
            else:
                cal[-1] *= 2
        elif i == '#':
            cal[-1] = cal[-1] * (-1)
    print(cal)

    return sum(cal)