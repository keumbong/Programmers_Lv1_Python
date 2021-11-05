###문제 설명###
#정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

###제한사항###
#numbers의 길이는 2 이상 100 이하입니다.
#numbers의 모든 수는 0 이상 100 이하입니다.

###입출력 예###
#numbers	    result
#[2,1,3,4,1]	[2,3,4,5,6,7]
#[5,0,2,7]	    [2,5,7,9,12]

from itertools import combinations

def solution(numbers):
    answer = []
    for combo in combinations(numbers, 2):
        answer.append(sum(combo))
    #중복제거
    answer_set = set(answer)
    answer_list = list(answer_set)
    #오름차순
    answer_list.sort()
    return answer_list

### permutations - 순열(순서O, 중복X)
#   permutations(iterable, n) - 반복가능한 객체 안에서 원소 개수가 n개인 순열
#   ex) permutations(list, 3),  permutations(range(1,11), 2)

### combinations - 조합(순서X, 중복X)
#   combinations(iterable, n) - 반복가능한 객체 안에서 원소 개수가 n개인 조합
#   ex) combinations(list, 3), combinations(range(1, 11), 3)

### product - 데카르트 곱(순서O, 중복O)
#   product(iterable, repeat = n) - 다른 함수들과 달리 객체에 여러 iterable을 넣을 수 있고, n에 따라 중복 횟수 결정 가능
#   ex) product(list1, list2, repeat = 1), product(list, repeat = 3)

### combinations_with_replacement - (순서X, 중복O)
#   combinations_with_replacement(iterable, n) - combinations에서 중복이 허용된 조합
#   ex) combinations_with_replacement(list, 2)
