# 중복된 문자 제거
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120888
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 02. 09. 09:49:03

def solution(my_string):
    answer = ''
    for i in my_string:
        if answer.find(i) < 0:
            answer += i
    return answer