# 숨어있는 숫자의 덧셈 (2)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120864
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 02. 26. 09:19:15

def solution(my_string):
    answer = 0
    temp = ''
    for i in my_string:
        if ord(i) <= 57:
            temp += i
        else:
            if temp != '':
                answer += int(temp)
                temp = ''
    if temp != '':
        answer += int(temp)
    return answer