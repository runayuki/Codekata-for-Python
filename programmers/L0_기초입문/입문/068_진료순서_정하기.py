# 진료순서 정하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120835
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 04. 02. 09:35:11

def solution(emergency):
    answer = []
    temp = emergency.copy()
    temp.sort(reverse = True)
    for value in emergency:
        for i, v in enumerate(temp):
            if value == v:
                answer.append(i + 1)
    return answer