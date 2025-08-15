# 벽 부수고 이동하기 4
'''
시간초과 로직
ouput 2차원 배열 만들어두기 - 여기에 정답 저장

- 값이 1이 칸에 대해 bfs 돌리기
    - pop할 때 마다 cnt += 1
    - 최종 cnt 값을 ouput[i][j]에 저장
'''
'''
시간초과 해결 로직
모든 벽에 대해 다~~ bfs돌리면 시간이 비효율적임 
    -> bfs 돌려지는건 0(빈칸)이니까 빈칸들로 한번만 bfs 돌려놓으면, 나중에 벽은 그 정보를 보고 합산만 해주면 됨
    
1. 빈 공간에 대해 bfs 돌리기
    - 이때 2부터 시작해서 같은 인접 빈공간은 같은 숫자로 인덱스 부여
    - 이때 딕셔너리에 저장 {2: 3, 3: 1, 4: 2}
2. 각 벽에 대해서 상하좌우 탐색하며 2이상인 칸이 있을 때, 딕셔너리에서 값 뽑아와서 다 더해서 ouput에 출력

'''
import sys; input = sys.stdin.readline
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
board = []
for _ in range(N) : board.append(list(map(int, input().strip())))
ouput = [[0 for _ in range(M)] for _ in range(N)]

def is_inrange(x, y) : 
    return 0<=x<N and 0 <= y < M 

def bfs(x, y, idx) : 
    cnt = 0
    que = deque()
    que.append((x, y))
    visited[x][y] = 1

    while que : 
        x, y = que.popleft()
        board[x][y] = idx
        cnt += 1
        for i in range(4) : 
            nx, ny = x + dx[i], y + dy[i]
            if is_inrange(nx, ny) and not visited[nx][ny] and board[nx][ny] == 0 : 
                que.append((nx, ny))
                visited[nx][ny] = 1
    
    return cnt 

dic = {}
visited = [[0 for _ in range(M)] for _ in range(N)]
index = 2
for i in range(N) :
    for j in range(M) : 
        if board[i][j] == 0 and not visited[i][j]: 
            count = bfs(i, j, index)
            dic[index] = count
            index += 1

for i in range(N) :
    for j in range(M) : 
        if board[i][j] == 1 : 
            result = 1
            v = set()
            for k in range(4) : 
                nx, ny = i + dx[k], j + dy[k]
                if is_inrange(nx, ny) and board[nx][ny] >= 2 and board[nx][ny] not in v: 
                    v.add(board[nx][ny])
                    result += dic[board[nx][ny]]
            ouput[i][j] = result % 10
                    

for i in range(N) :
    for j in range(M) : 
        print(ouput[i][j], end="")
    print()