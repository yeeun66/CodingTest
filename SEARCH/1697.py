# 숨바꼭질 ---- 아직 푸는 중

# 수빈이는 현재 점 N에 있고, 동생은 점 K에 있다.
# 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동, 순간이동을 하면 1초 후에 2*X의 위치로 이동
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램

# 알고리즘 정리만 하고 나중에 풀자
# 큐에 3가지 경우씩 다 집어 넣어. 언제까지? 5배 할 때는 동생 위치의 2배부터는 5배 안하도록
# 하나씩 pop 하면서 동생위치인지 검사하고 아니면 또 집어넣어
# 그리고 몇 초만에 찾았는지 알려면 새로운 리스트에 표시를 할 건데 pop한 인덱스번째에 0이었다가 한번 pop을 했으면 증가시켜. 그럼 최종 엥 이거 모르겠다.
 
import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())

def bfs() : 

    queue = deque([N])
    visit = [0]*100,000
    while queue :
        cur = queue.popleft()
        if not visit[cur]: 
            queue.append((cur-1, cur+1, cur*2))
            visit[cur] = True