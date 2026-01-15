def solution(n): 
    answer = 0
    temp = n
    while temp > 0:
        if n % temp == 0:
            answer += temp
        temp -= 1
    return answer