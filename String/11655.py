# ROT13
# 문자열을 아스키코드 순으로 13글자 씩 밀어서 암호화 
# (대소문자 각각 따로, 알파벳 아닌 것은 그대로)

# 반례) 첫 공백시의 공백도 고려해야함 -> strip('\n') 이걸로 해야 공백 안없어짐
import sys
input= sys.stdin.readline

string = input().strip('\n')
arr = []
for i in string :
    if i.isupper() :
        gap = 13
        if ord(i) + gap > 90 :
            gap = ord(i) + gap - 90 - 1
            i = chr(65 + gap)
        else : i = chr(ord(i) + gap)
        arr.append(i)
    elif i.islower() :
        gap = 13
        if ord(i) + gap > 122 :
            gap = ord(i) + gap - 122 - 1
            i = chr(97 + gap)
        else : i = chr(ord(i) + gap)
        arr.append(i) 
    else : arr.append(i)

answer = "".join(arr)
print(answer)