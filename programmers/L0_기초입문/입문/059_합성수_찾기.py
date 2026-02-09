# 합성수 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120846
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 02. 09. 09:47:11

def solution(n):
    answer = 0
    count = 0
    for i in range(1, n + 1):
        for r in range(1, i + 1):
            if i % r == 0:
                count += 1
        if count >= 3:
            answer += 1
        count = 0
    return answer