# 배열 회전시키기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120844
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 02. 06. 09:44:34

def solution(numbers, direction):
    answer = []
    if direction == 'right':
        temp = numbers[-1]
        numbers = numbers[:-1]
        answer.append(temp)
        answer += numbers
    else:
        temp = numbers[0]
        numbers = numbers[1:]
        numbers.append(temp)
        answer = numbers
    return answer