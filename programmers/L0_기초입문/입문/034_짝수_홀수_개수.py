# 짝수 홀수 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120824
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 01. 21. 09:22:54

def solution(num_list):
    answer = []
    e_count = o_count = 0
    for i in num_list:
        if i % 2 == 0:
            e_count += 1
        else:
            o_count += 1
    answer.append(e_count)
    answer.append(o_count)
    return answer