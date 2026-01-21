# 개미 군단
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120837
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 01. 21. 09:48:27

def solution(hp):
    answer = 0
    damage = 0
    if hp // 5 >= 1:
        damage = ( hp // 5 ) * 5
        answer += hp // 5
        hp -= damage
    if hp // 3 >= 1:
        damage = (hp // 3) * 3
        answer += hp // 3
        hp -= damage
    if hp > 0:
        answer += hp
    return answer