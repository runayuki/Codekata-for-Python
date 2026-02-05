# 약수 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120897
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 02. 05. 09:12:48

def solution(n):
    answer = []
    i = 1
    while i <= n:
        if n % i == 0:
            answer.append(i)
        i += 1
    return answer