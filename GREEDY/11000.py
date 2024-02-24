# 강의실 배정 -- 아직 안품

# 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다. 
# 참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)

# 강의실의 개수를 출력
# 회의실 문제 처럼 끝 시간 순으로 정렬 후, 가능한 수업 표시 후 강의실 수 카운트 후, 사용한 수업은 pop하고 
# 다시 가능한 수업 찾고 강의실 수 카운트 <- 수업 개수 0 될 때까지

# 런타임 에러? 이젠 시간 초과 
# 우선순위 큐 써야 하나?
# 큐엠티까지 다음을 반복
# ???

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
que = deque()
for _ in range(N) :
    a, b = map(int, input().split())
    que.append((b, a))
print(que)
count = 0

end, st = que.popleft()
while que :
    x, y = que.popleft()
    start = y
    if start > end : 

if N == 1 : print(count+1)
else: print(count)
# count = 0
# while len(d) != 0 :
#     n = len(d)
#     end = d[0][0]
#     d[0] = (-1, -1)
#     if n == 1 : 
#         count += 1
#         break
#     for i in range(1, n) :
#         start = d[i][1]
#         if end > start : continue
#         end = d[i][0]
#         d[i] = (-1, -1)
    
#     remove_set = {(-1, -1)}
#     d = [k for k in d if k not in remove_set] # remove_set에 없는 데이터만 새로운 리스트에 저장하여 특정 값을 제거하는 효과
#     count += 1

print(count)