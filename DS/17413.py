# 문자열 S가 주어졌을 때, 이 문자열에서 단어만 뒤집으려고 한다.
# 태그는 단어가 아니며, 태그와 단어 사이에는 공백이 없다.
# 입력: <int><max>2147483647<long long><max>9223372036854775807
# 출력: <int><max>7463847412<long long><max>7085774586302733229
# 입력: <ab cd>ef gh<ij kl>
# 출력: <ab cd>fe hg<ij kl>

# 로직
# 반복문 하나와 스택 하나(스택은 문자열 뒤집는 용도)
# 만약 '<' 이면, open 상태/ '>'이면 close 상태
# open 상태일 때
#   스택 empty면, 그냥 output에 추가
#   스택 nonempty면, 스택을 거꾸로 뒤집고 리스트로 바꿔서 뒤집어서 output에 추가
    # 그러고 stk=""로 비우기
# close 상태이면 스택에 추가

# 반복문 끝난 후 스택 nonempty면 스택을 거꾸로 뒤집고 리스트로 바꿔서 뒤집어서 output에 추가
# 이후 output 출력

import sys
input = sys.stdin.readline

s = input().strip()
output = ""
stk = ""
in_tag = False  # 태그 안에 있는지 여부를 나타내는 플래그

for char in s:
    if char == '<':  # 태그의 시작
        # 태그 전에 쌓인 단어를 뒤집어 추가
        output += stk[::-1]
        stk = ""
        in_tag = True
        output += char
    elif char == '>':  # 태그의 끝
        in_tag = False
        output += char
    elif in_tag:  # 태그 안에 있는 경우 그대로 추가
        output += char
    elif char == ' ':  # 단어와 단어 사이의 공백 처리
        output += stk[::-1] + ' '
        stk = ""
    else:
        stk += char  # 태그 밖에서 단어를 쌓아두기

# 마지막 단어 처리 (태그가 아닌 경우 남아있을 수 있는 stk 뒤집기)
output += stk[::-1]

print(output)
