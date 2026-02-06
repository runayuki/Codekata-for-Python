# 피자 나눠 먹기 (2)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120815
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 02. 06. 09:26:42

def solution(n):
    answer = 0
    i = 1
    while True:
        if i * 6 % n == 0:
            answer = i
            break
        i += 1
    return answer