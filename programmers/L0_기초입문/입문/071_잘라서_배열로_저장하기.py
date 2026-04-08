# 잘라서 배열로 저장하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120913
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 04. 08. 09:42:44

def solution(my_str, n):
    answer = []
    start = 0
    end = n
    if len(my_str) % n > 0:
        length = (len(my_str) // n) + 1
    else:
        length = len(my_str) // n
        
    for i in range(1, length + 1):
        if i == length:
            answer.append(my_str[start : ])
        else:
            answer.append(my_str[start : end])
            start = end
            end = n * (i + 1)
    return answer