# 문자열 계산하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120902
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 04. 10. 10:13:41

def solution(my_string):
    answer = 0
    minus = False
    string = my_string.split(sep = ' ')
    for i in string:
        if i == '+':
            minus = False
        elif i == '-':
            minus = True
        else:
            if minus:
                answer -= int(i)
            else:
                answer += int(i)
    return answer