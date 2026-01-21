# 모음 제거
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120849
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 01. 21. 09:18:27

def solution(my_string):
    first = my_string.replace('a', '')
    second = first.replace('e', '')
    third = second.replace('i', '')
    fourth = third.replace('o', '')
    answer = fourth.replace('u', '')
    return answer