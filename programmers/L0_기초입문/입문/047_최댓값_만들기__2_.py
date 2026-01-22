# 최댓값 만들기 (2)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120862
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 01. 22. 13:42:08

def solution(numbers):
    numbers.sort(reverse = True)
    answer = numbers[0] * numbers[1]
    if numbers[-1] * numbers[-2] > answer:
        answer = numbers[-1] * numbers[-2]
    return answer