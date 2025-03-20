# 빙산
# 한 덩어리의 빙산이 주어질 때, 이 빙산이 두 덩어리 이상으로 분리되는 최초의 시간(년)을 구하는 프로그램을 작성
# 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면, 0을 출력

# 입력에서 배열의 첫 번째 행과 열, 마지막 행과 열에는 항상 0으로 채워진다. << 고 했으므로
    # 첫번째 배열부터 탐색 시작가능할듯

# 1. 입력 받고 리스트에 저장
# 2. BFS (0, 0) 부터 탐색 시작 (큐 엠티까지 다음을 반복)
    # 하나씩 pop 하며 상하좌우 탐색
        # 현재 값이 0이고, 탐색한 값이 0보다 클 때, 값 하나 줄임
        # 모든 경우에, 탐색 값 방문 전이면 -> 큐에 넣고 방문 표시
# 3. 2번에서 만들어진 리스트로 덩어리 갯수 세기 (DFS)
    # dfs 활용해서 연결 요소 갯수 세기 (stk)
# 4. 덩어리 갯수가 2개 이상이 될 때 까지 2,3번 반복
    # 덩어리 갯수가 2이상이면 -> 반복횟수 출력 및 종료
    # 2미만인데 배열 값의 합이 0이면 -> 0 출력 및 종료
    # 2미만인데 배열 값의 합이 0보다 크면 다시 반복

# 시간 초과.. PyPy3으로 제출하니까 통과됨.. 뭐지
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
arr = []

for _ in range(N) :
    arr.append(list(map(int, input().split())))

def bfs() :
    que = deque()
    que.append((0, 0))
    visit = [[0] * M for _ in range(N)]
    visit[0][0] = 1

    while que :  # 감소 시켜서 0이 되면, 0이 아니라 -1로 만들자, 1년 뒤에는 0으로 만드는 작업 함수 밖에서 해야 함
        x, y = que.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M :
                if arr[x][y] == 0 and arr[nx][ny] > 0 : 
                    arr[nx][ny] -= 1
                    if arr[nx][ny] == 0 : arr[nx][ny] = -1
                if visit[nx][ny] == 0 : 
                    visit[nx][ny] = 1
                    que.append((nx, ny))

def dfs(x, y) :
    stk = []
    stk.append((x, y))
    vis[x][y] = 1
    while stk :
        x, y = stk.pop()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M :
                if arr[nx][ny] > 0 and vis[nx][ny] == 0 :
                    vis[nx][ny] = 1
                    stk.append((nx, ny))
        
year = 0
while True :
    block = 0
    vis = [[0] * M for _ in range(N)]
    for i in range(N) : # DFS
        for j in range(M) :
            if arr[i][j] > 0 and vis[i][j] == 0 : 
                dfs(i, j)
                block += 1

    if block >= 2 : 
        print(year)
        break
    else : 
        sums = 0
        for i in range(N) :
            sums += sum(arr[i])
        if sums <= 0 : 
            print(0)
            break
    
    bfs() # BFS
    year += 1
    for i in range(N) :
        for j in range(M) :
            if arr[i][j] == -1 : arr[i][j] = 0