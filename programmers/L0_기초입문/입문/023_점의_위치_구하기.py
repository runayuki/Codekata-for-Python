# 점의 위치 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120841
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 01. 19. 09:32:46

def solution(dot):
    if dot[0] > 0:
        if dot[1] > 0:
            answer = 1
        else:
            answer = 4
    else:
        if dot[1] > 0:
            answer = 2
        else:
            answer = 3
    return answer