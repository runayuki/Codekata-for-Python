# 배열 뒤집기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120821
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 01. 16. 09:35:23

def solution(num_list):
    answer = []
    
    for i in num_list[::-1]:
        answer.append(i)
    
    return answer