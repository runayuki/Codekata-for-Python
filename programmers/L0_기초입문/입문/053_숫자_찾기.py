# 숫자 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120904
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 02. 05. 09:46:05

def solution(num, k):
    num_s = str(num)
    if num_s.find(str(k)) >= 0:
        answer = num_s.find(str(k)) + 1
    else:
        answer = -1
    return answer