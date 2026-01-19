# 세균 증식
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120910
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 01. 19. 09:22:32

def solution(n, t):
    for i in range(t):
        n *= 2
    
    answer = n
    return answer