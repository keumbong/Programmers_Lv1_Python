import math
def solution(n, m):
    answer = []
    gcd = math.gcd(n, m) #최대공약수 math.gcd
    #lcm = math.lcm(n, m) 최소공배수 math.lcm 3.9버전 부터
    lcm = (n * m) / gcd
    answer += gcd,lcm
    return answer