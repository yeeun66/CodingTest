# 파일에는 단어가 한 줄에 하나씩 적혀있었고, 이 중 하나는 민균이가 온라인 저지에서 사용하는 비밀번호이다.
# 모든 단어의 길이가 홀수
# 비밀번호는 목록에 포함되어 있으며, 비밀번호를 뒤집어서 쓴 문자열도 포함
#   Ex) 비밀번호가 "tulipan"인 경우에 목록에는 "napilut"도 파일에 존재함
#       kisik 이렇게 거꾸로 바꿔도 똑같은 것도 가능
# 파일에 적혀있는 단어가 모두 주어졌을 때, 비밀번호의 길이와 가운데 글자를 출력하는 프로그램을 작성

# 반복문 돌면서 해당 문자열은 거꾸로 한 다음에 나머지와 비교.
# 비번 발견하면 길이 세고, 가운데 글자 추출

import sys
input = sys.stdin.readline

N = int(input())
s = set([input().strip() for _ in range(N)]) # strip() 은 개행 문자 제거
    
for i in range(N) :
    string = list(s)[i]
    string = string[::-1]
    if string in s :
        l = len(string)
        center = int((l-1)/2)
        print(l, string[center])
        break