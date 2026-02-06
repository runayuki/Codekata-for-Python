# 외계행성의 나이
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120834
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 02. 06. 09:36:17

def solution(age):
    answer = []
    while age > 0:
        temp = age % 10
        answer.append(chr(temp + 97))
        age //= 10
    
    answer.reverse()
        
    return ''.join(answer)