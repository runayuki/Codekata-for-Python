# 문자열 정렬하기 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120850
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 01. 22. 13:38:12

def solution(my_string):
    answer = []
    for i in my_string:
        if not i.isalpha():
            answer.append(int(i))
    answer.sort()
    return answer