# 컨트롤 제트
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120853
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 04. 08. 11:49:50

def solution(s):
    answer = 0
    last = 0
    num_list = s.split(sep = ' ')
    for i in num_list:
        if i == 'Z':
            answer -= last
        else:
            answer += int(i)
            last = int(i)
    return answer