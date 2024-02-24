# 회의실 배정
# 최대 사용할 수 있는 회의의 최대 개수를 출력
# (회의의 시작시간과 끝나는 시간이 같을 수도 있다)

# 그냥 로직 다시 생각하기
# 끝나는 시간 순으로 정렬해서 처음부터 카운트 한 번만 하면 됨

import sys
input = sys.stdin.readline

n = int(input())
d = []
for i in range(n) :
    a, b = map(int, input().split())
    d.append((b, a))

d.sort()

count = 1
end = d[0][0] #  첫 회의 끝 시간
for i in range(1, n) :
    start = d[i][1] # 다음 회의 시작 시간
    if end <= start : 
        count += 1
        end = d[i][0]

print(count)