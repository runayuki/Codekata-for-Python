# n의 배수 고르기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120905
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 01. 19. 09:58:10

def solution(n, numlist):
    len_num = len(numlist)
    i = 0
    while i < len_num:
        if numlist[i] % n > 0:
            del numlist[i]
            len_num -= 1
            i -= 1
        i += 1
        
    answer = numlist
    return answer