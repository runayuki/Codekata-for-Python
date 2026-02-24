# 한 번만 등장한 문자
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120896
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 02. 24. 09:46:29

def solution(s):
    answer = ''
    for i in s:
        filter_list = list(filter(lambda x: x == i, s))
        if len(filter_list) == 1:
            answer += filter_list[0]
            
    answer = ''.join(sorted(answer))
    return answer