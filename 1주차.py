def solution(price, money, count):
    cost = 0
    for i in range(1, count + 1):
        cost += (price * i)

    return -(money - cost) if money < cost else 0