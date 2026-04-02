# 가까운 수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120890
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 04. 02. 09:42:18

def solution(array, n):
    answer = array[0]
    diff = abs(n - array[0])
    for i in array[1:]:
        if abs(n - i) < diff: 
            answer = i
            diff = abs(n - i)
        elif abs(n - i) == diff:
            if answer > i:
                answer = i
    return answer