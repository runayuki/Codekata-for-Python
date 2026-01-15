def solution(n):
    answer = temp = n - 1
    while temp > 0:
        if n % temp == 1:
            if answer > temp:
                answer = temp
        temp -= 1
    return answer