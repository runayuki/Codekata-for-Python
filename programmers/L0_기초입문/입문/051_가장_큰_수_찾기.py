# 가장 큰 수 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120899
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 02. 05. 09:18:06

def solution(array):
    array_sort = sorted(array)
    idx = array.index(array_sort[-1])
    answer = [array_sort[-1], idx]
    return answer