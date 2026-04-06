# 팩토리얼
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120848
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 04. 06. 09:17:47

def solution(n):
    answer = 1
    result = 1
    while 1:
        for i in range(1, answer + 1):
            result *= i
        if result > n:
            answer -= 1
            break
        elif result == n:
            break
        result = 1
        answer += 1
    return answer