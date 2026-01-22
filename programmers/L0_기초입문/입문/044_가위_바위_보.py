# 가위 바위 보
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120839
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 01. 22. 11:48:59

def solution(rsp):
    answer = ''
    for i in rsp:
        if i == '0':
            answer += '5'
        elif i == '2':
            answer += '0'
        else:
            answer += '2'
    return answer