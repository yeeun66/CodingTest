# 2차원 배열
# 문자열 세로로 읽은 순서대로 글자들을 공백 없이 출력

# 입력
# ABCDE
# abcde
# 01234
# FGHIJ
# fghij

# 출력
# Aa0FfBb1GgCc2HhDd3IiEe4Jj

str = []
for _ in range(5) :
    str.append(input())

num = []
for sublist in str:
    num.append(len(sublist))

max = max(num)
new_str = [[None] * 5 for _ in range(max)] # 6x5 크기의 빈 배열 생성

for i in range(5) :
    for j in range(num[i]) :
        new_str[j][i] = str[i][j]

result = ''
for i in range(max) :
    for j in range(5) :
        if new_str[i][j] is not None :
            result += new_str[i][j]
        
print(result)