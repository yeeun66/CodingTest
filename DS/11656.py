# 정렬 문제
# 문자열 S가 주어졌을 때, 모든 접미사를 사전순으로 정렬한 다음 출력하는 프로그램을 작성하시오.
# baekjoon의 접미사는 baekjoon, aekjoon, ekjoon, kjoon, joon, oon, on, n 으로 총 8가지가 있고, 
# 이를 사전순으로 정렬하면, aekjoon, baekjoon, ekjoon, joon, kjoon, n, on, oon이 된다.
#
# 로직
# 문자열 s에 대해, 접미사(suffix) list에 추가 후, 앞에서 부터 pop()해서 suffix list 만들기
# 걍 suffix.sort() => 이게 되네?

import sys
input = sys.stdin.readline

s = input().strip()
suffix = []
length = len(s)
for i in range(length):
    string = ""
    for j in range(i, length) :
        string += s[j]
    suffix.append(string)

suffix.sort()

for a in suffix : print(a)