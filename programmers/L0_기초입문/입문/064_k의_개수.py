# k의 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120887
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 02. 23. 12:27:25

def solution(i, j, k):
    answer = 0
    for a in range(i, j + 1):
        a = str(a)
        for b in a:
            if int(b) == k:
                answer += 1
    return answer