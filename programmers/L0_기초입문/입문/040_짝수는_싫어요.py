# 짝수는 싫어요
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120813
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 01. 21. 09:34:41

def solution(n):
    answer = []
    for i in range(n + 1):
        if i % 2 > 0:
            answer.append(i)
    return answer