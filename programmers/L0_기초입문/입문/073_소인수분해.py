# 소인수분해
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120852
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 04. 09. 10:43:32

def solution(n):
    answer = []
    num = n
    while num != 1:
        for i in range(2, num + 1):
            if num % i == 0:
                if not(i in answer):
                    answer.append(i)
                num /= i 
                num = int(num)
                break
    return answer