def solution(new_id):
    answer = ''

    # step1
    new_id = new_id.lower()

    # step2
    for word in new_id:
        if word.isalnum() or word in '-_.':
            answer += word

    # step3
    while '..' in answer:
        answer = answer.replace('..', '.')

    # step4
    answer = answer.strip('.')

    # step5
    answer = 'a' if answer == '' else answer

    # step6
    if len(answer) >= 16:
        if answer[14] == ".":
            answer = answer[:14]
        else:
            answer = answer[:15]

    # step7
    while len(answer) < 3:
        answer += answer[-1]

    return answer