# 총 N개의 문자열로 이루어진 집합 S가 주어진다.
# 입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
s = set([input() for _ in range(N)]) # 집합 S => 중복 허용 안하기 때문에 더 효율적으로 단어 저장 가능

# 이제 나머지 M개 입력 바로 받아서 입력이 S에 포함되는지 알아보기
cnt = 0
for i in range(M) :
    x = input()
    if x in s :
        cnt += 1
        print("x: ", x)

print(cnt)