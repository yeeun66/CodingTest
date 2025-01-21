# 스타트링크
# 스타트링크는 총 F층으로 이루어진 고층 건물에 사무실이 있고, 스타트링크가 있는 곳의 위치는 G층이다. 
# 강호가 지금 있는 곳은 S층이고, 이제 엘리베이터를 타고 G층으로 이동하려고 한다.

# 강호가 탄 엘리베이터는 버튼이 2개밖에 없다. U버튼은 위로 U층을 가는 버튼, D버튼은 아래로 D층을 가는 버튼이다. 
# (만약, U층 위, 또는 D층 아래에 해당하는 층이 없을 때는, 엘리베이터는 움직이지 않는다)
# 강호가 G층에 도착하려면, 버튼을 적어도 몇 번 눌러야 하는지 구하는 프로그램을 작성하시오.
# 만약, 엘리베이터를 이용해서 G층에 갈 수 없다면, "use the stairs"를 출력한다.

# 방법: 
# 1. 1차원 배열 및 변수 초기화
    # 1차원 배열 F+1 크기로 모두 0으로 초기화
    # 처음부터 S == G 이면 탐색X. 그냥 0 출력
# 2. bfs 탐색
    # S부터 bfs 탐색 시작 ()
    # S부터 큐에 넣고 다음을 반복 
        # 반복문 두번 돌면서 x값 변화시킨다
            # 첫번째로는 nx = x + U
            # 두번째는 nx = x - D
        # 해당 nx 값이 F를 초과하거나 0 이하가 되면 계단 쓰세요 출력하고 리턴
        # 해당 nx 값이 G와 같으면 (부모 노드 + 1) 값 출력하고 리턴
        # nx 값이 1~F 사이일 때 해당 값이 0이면 (부모 노드 + 1) 값 저장 후, 큐에 넣기

import sys
from collections import deque
input = sys.stdin.readline

def bfs(s) :
    queue = deque([s])

    while queue :
        x = queue.popleft()
        # print('x: ', x)
        for i in range(2) :
            if i == 0 : nx = x + U
            else : nx = x - D

            if nx <= 0 or nx > F : 
                if queue or i == 0 : continue
                else :
                    print("use the stairs")
                    return
            if nx == G : 
                print(graph[x])
                return
            
            if 1 <= nx <= F and graph[nx] == 0 : 
                graph[nx] = graph[x] + 1
                queue.append(nx)

    print("use the stairs") # 범위 초과하지 않고도 queue가 빌 수 있음
            
arr = list(map(int, input().split()))
F = arr[0]
S = arr[1]
G = arr[2]
U = arr[3]
D = arr[4]

graph = [0] * (F+1)
graph[S] = 1
if S == G : print(0)
else : bfs(S)    