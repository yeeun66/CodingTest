# Two Dots
'''
DFS로 사이클 판별하는 법: 
    현재 노드에서 탐색할 이웃 노드 중 이미 방문한 노드가 있다면, 
    그런데 그 노드가 바로 이전 부모노드가 아니라면 사이클이 존재

1. DFS 탐색
2. 방문하지 않은 노드라면 방문 처리 후, 스택에 추가
3. 방문되어 있는 노드라면, 그 노드가 현재 노드의 부모노드가 아니라면 사이클 존재 -> Yes 출력 후 종료
    - 이거 구현을 위해 스택에 좌표와 함께 부모 노드의 좌표도 함께 넣어줌

모든 노드 탐색 끝나도 종료 안되었으면, No 출력

'''

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, input().split())
board = []
for _ in range(N) : board.append(list(map(str, input().strip())))

def is_inrange(x, y) : 
    return 0<= x < N and 0 <= y < M 

visited = [[0 for _ in range(M)] for _ in range(N)]
def dfs(x, y) : # depth가 4 이상일 때, 방문 했던 것 또 방문하려 하면, 사이클 존재
    stk = []
    color = board[x][y]
    stk.append((x, y, -1, -1))
    visited[x][y] = 1
    while stk : 
        x, y, px, py = stk.pop()
        for i in range(4) : 
            nx, ny = x + dx[i], y + dy[i]
            if is_inrange(nx, ny) and board[nx][ny] == color: 
                if not visited[nx][ny] : 
                    stk.append((nx, ny, x, y)) # 자신 / 부모
                    visited[nx][ny] = 1
                else : 
                    if (nx, ny) != (px, py) : 
                        print('Yes')
                        exit()
    

for i in range(N) : 
    for j in range(M) :
        if not visited[i][j] : 
            dfs(i, j)

print('No')
