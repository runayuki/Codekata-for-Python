# A로 B 만들기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120886
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 02. 23. 09:27:28

def solution(before, after):
    for i in before:
        if after.find(i) >= 0:
            after = after.replace(i, '', 1)
    answer = 1 if after == '' else 0
    return answer