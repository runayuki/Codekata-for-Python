# 모스부호 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120838
# 알고리즘: 기초
# 작성자: 박수빈
# 작성일: 2026. 02. 12. 09:26:32

def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }
    letter_s = list(letter.split())
    answer = ''
    for i in letter_s:
        for key, value in morse.items():
            if key == i:
                answer += value
                break
    return answer