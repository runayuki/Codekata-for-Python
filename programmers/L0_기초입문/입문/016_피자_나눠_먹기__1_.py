# 피자 나눠 먹기 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120814
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 01. 16. 09:40:26

def solution(n):
    answer = int(n // 7)
    if n % 7 >= 1:
        answer += 1
    return answer