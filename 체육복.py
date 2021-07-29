def solution(n, lost, reserve):
    reserve_r = set(reserve) - set(lost)
    lost_r = set(lost) - set(reserve)
    answer = n - len(lost_r)
    for i in lost_r:
        if i-1 in reserve_r: #잃어버린 사람 왼쪽 확인
            answer += 1
            reserve_r.remove(i-1)
        elif i+1 in reserve_r: #잃어버린 사람 오른쪽 확인
            answer += 1
            reserve_r.remove(i+1)