# 숨바꼭질

# 수빈이는 현재 점 N에 있고, 동생은 점 K에 있다.
# 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동, 순간이동을 하면 1초 후에 2*X의 위치로 이동
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램

# 방법: 이것도 상하좌우 확장판
# 이건 2차원 좌표가 아니라 선형 이동인 것 같고 수빈이가 N에서 +1, -1 또는 *2 만큼 이동 가능하니까 이 3가지 경우를 bfs로 반복한다. 
# 반복하면서 동생의 위치를 찾으면 루트 노드의 값 + 1 출력
# 1. 그래프 초기화
    # (100001) 크기의 1차원 배열 생성 후 모두 0으로 초기화
    # 수빈이의 위치에서 bfs 시작
    # 동생 위치에는 -100 넣기
    # 처음부터 N, K 같았다면 그냥 0 출력하고 종료
# 2. BFS 탐색
    # 3번 반복 하면서
    # 값이 -100인걸 만나면(동생 찾으면), 부모 노드 + 1 값을 리턴
    # 방문하지 않은 곳이면, 방문 표시(부모 노드 + 1)하고 큐에 추가

import sys
from collections import deque
input = sys.stdin.readline

def bfs(N) : 
    queue = deque()
    queue.append(N)

    while queue : 
        cur = queue.popleft()
        for i in range(3) :
            if i == 0 : n = cur+1
            elif i == 1 : n = cur-1
            else : n = cur*2

            if 0 <= n < 1000001 : 
                if graph[n] == -100 : return (graph[cur] + 1)
                elif graph[n] == 0 : 
                    graph[n] = graph[cur] + 1
                    queue.append(n)


N, K = map(int, input().split())
graph = [0] * (1000001)
graph[K] = -100 # 동생

if N == K : print(0)
else : print(bfs(N))