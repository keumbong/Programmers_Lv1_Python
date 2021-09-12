import re
def solution(phone_number):
    phone = phone_number[-4:]
    vail_num = re.sub('[0-9]','*',phone_number[0:-4])
    answer = vail_num + phone
    return answer