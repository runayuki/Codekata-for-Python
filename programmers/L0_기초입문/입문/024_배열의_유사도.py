# 배열의 유사도
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120903
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 01. 19. 09:33:39

def solution(s1, s2):
    answer = 0
    for i in s1:
        for r in s2:
            if i == r:
                answer += 1
    return answer