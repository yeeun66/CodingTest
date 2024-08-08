# 서로 다른 부분 문자열의 개수
# 문자열 S가 주어졌을 때, S의 서로 다른 부분 문자열의 개수를 구하는 프로그램을 작성
# 부분 문자열은 S에서 연속된 일부분을 말하며, 길이가 1보다 크거나 같아야 한다.
# 예를 들어, ababc의 부분 문자열은 a, b, a, b, c, ab, ba, ab, bc, aba, bab, abc, abab, babc, ababc가 있고, 서로 다른것의 개수는 12개이다.

# 부분 문자열 생성 후, set에 때려넣기
import sys
input = sys.stdin.readline

a = input().strip()
s = set()
l = len(a)
for start in range(l) :
    for end in range(1, l+1) :
        s.add(a[start:end])

if '' in s :
    s.remove('')

print(len(s))