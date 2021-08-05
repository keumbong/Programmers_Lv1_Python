def solution(numbers, hand):
    answer = ''
    left_last = 10
    right_last = 12

    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            left_last = i
        elif i in [3, 6, 9]:
            answer += 'R'
            right_last = i
        else:
            i = 11 if i == 0 else i
            left_abs = abs(i - left_last)
            right_abs = abs(i - right_last)

            if sum(divmod(left_abs, 3)) > sum(divmod(right_abs, 3)):
                answer += 'R'
                right_last = i
            elif sum(divmod(left_abs, 3)) < sum(divmod(right_abs, 3)):
                answer += 'L'
                left_last = i
            else:
                if hand == 'left':
                    answer += 'L'
                    left_last = i
                else:
                    answer += 'R'
                    right_last = i

    return answer