# 대문자와 소문자
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120893
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 02. 06. 09:22:00

def solution(my_string):
    answer = []
    for i in my_string:
        if ord(i) >= 97:
            answer.append(chr(ord(i) - 32))
        else:
            answer.append(chr(ord(i) + 32))
    return ''.join(answer)