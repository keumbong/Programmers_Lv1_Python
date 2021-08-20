def solution(s):

    countP, countY = 0, 0

    for i in range(len(s)):
        if s[i] == 'P' or s[i] == 'p':
            countP += 1
        if s[i] == 'Y' or s[i] == 'y':
            countY += 1

    return True if countP == countY else False