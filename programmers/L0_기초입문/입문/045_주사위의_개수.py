# 주사위의 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120845
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 01. 22. 13:32:52

def solution(box, n):
    answer = (box[0] // n) * (box[1] // n) * (box[2] // n) 
    return answer