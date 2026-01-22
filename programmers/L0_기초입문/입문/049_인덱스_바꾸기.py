# 인덱스 바꾸기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120895
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 01. 22. 13:52:16

def solution(my_string, num1, num2):
    answer = my_string[:num1] + my_string[num2] + my_string[num1 + 1: num2] + my_string[num1] + my_string[num2 + 1:]
    return answer