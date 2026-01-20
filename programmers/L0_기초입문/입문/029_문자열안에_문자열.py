# 문자열안에 문자열
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120908
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 01. 20. 09:56:26

def solution(str1, str2):
    if str1.find(str2) >= 0:
        answer = 1
    else:
        answer = 2
    return answer