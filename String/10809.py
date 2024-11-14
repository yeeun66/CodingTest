# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 
# 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 
# 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성
# 입력: baekjoon
# 출력: 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1

# 로직:
# 출력 배열 -1로 초기화 (길이 27)
# 입력 받은 s 만큼 반복문 돌면서
    # 해당 인덱스의 번호를 출력 인덱스에 
        # 인덱스 결정은 아스키코드 'a'와의 차이로 결정
    # s에서 해당 문자와 같은 문자가 있는 경우 다 A로 만들어버림
    
import sys
input = sys.stdin.readline

s = list(map(str, input().strip()))
out = [-1] * 26

for i in range(len(s)) :
    if s[i] >= 'a' and s[i] <= 'z' : 
        index = ord(s[i]) - ord('a')
        out[index] = i
        if i < len(s) -1 :
            for j in range(i+1, len(s)) :
                if s[j] == s[i] :
                    s[j] = 'A'

print(*out)