def solution(n):
    answer = []
    temp = 0
    while n > 0:
        temp = n % 10
        answer.append(temp)
        n //= 10
    return answer