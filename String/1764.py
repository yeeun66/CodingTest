# 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성

# 첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M
# 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다.

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

listen = set()
see = set()
for _ in range(N) :
    listen.add(input().strip())
for _ in range(M) :
    see.add(input().strip())

cnt = 0

result = set()
result = listen & see
re = list(result)
re.sort()

print(len(re))
print('\n'.join(re))