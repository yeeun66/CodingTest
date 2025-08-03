# 열쇠
# 상근이가 훔칠 수 있는 문서의 최대 개수 구하기
# 이거 좀 어렵다 - TC 다 뒤져가며.. 겨우 맞춤 
# 문제는 새로운 열쇠 찾을 때, 그냥 방문처리를 부모+1 해줘서 방문처리 상태가 꼬였음
# => 새로운 열쇠 발견할 때 마다 방문처리 초기화해서 해결!!!

'''
로직 
1. 빌딩 밖에서 안으로 들어가는 입구 찾기
    - 입구는 빈칸이거나 열쇠(소문자)만 가능
    - 입구가 없으면 그냥 0 출력 후 종료
2. 일단 먹을 수 있는 열쇠를 최대한 다 먹어
    - bfs로 탐색하되, 
    -새로운 열쇠 발견할 때 마다 방문처리 초기화
3. 다 먹은 상태로 돌아다니며 문서 찾기
    - 이건 일반적인 bfs
    - 처음에 저장 해뒀던 입구를 큐에 넣고, 모두 찾은 열쇠 집합은 그냥 전역에 넣어두며, 갈 수 있으면 계속 가서 최대한 문서 다 먹기
'''

from collections import deque
import copy
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
T = int(input())

for _ in range(T) : 
    h, w = map(int, input().split())
    board = []
    for _ in range(h) : board.append(list(map(str, input().strip())))
    tmp = str(input())
    init_key = set()
    if tmp != '0' : 
        for t in tmp : init_key.add(t)
    # 1. 입구 찾기
    result = 0
    entrance = []
    for i in range(h) : 
        for j in range(w) : 
            if i == 0 or i == h-1 or j == 0 or j == w-1:
                if board[i][j] == '.' :
                    entrance.append((i, j))
                if board[i][j] == '$' :
                    entrance.append((i, j))
                    result += 1
                    board[i][j] = '.'
                if board[i][j].islower() :
                    entrance.append((i, j))
                    init_key.add(board[i][j])
                if board[i][j].isupper() : # 입구 대문자여도 열쇠 있으면 들어갈 수 있음 
                    entrance.append((i, j))
    
    if not entrance : 
        print(0)
        continue

    # 2. 먹을 수 있는 열쇠 다 먹기 
    que = deque()
    visited = [[0 for _ in range(w)] for _ in range(h)]
    cnt = len(init_key) + 1
    for i, j in entrance : 
        que.append((i, j))
        visited[i][j] = cnt
    
    while que : 
        x, y = que.popleft()
        if board[x][y].isupper() and board[x][y].lower() not in init_key : continue
        for i in range(4) : 
            nx, ny = x + dx[i], y + dy[i]
            if 0<= nx < h and 0 <= ny < w and not visited[nx][ny]:
                
                string = board[nx][ny]
                if string == '*' : continue
                if string == '$' or string == '.' : 
                    que.append((nx, ny))
                    visited[nx][ny] = 1

                    continue
                if string.isupper() :
                    if string.lower() not in init_key : continue
                    else : 
                        que.append((nx, ny))
                        visited[nx][ny] = 1
                        continue
                if string.islower() :
                    if string not in init_key : 
                        init_key.add(string)
                        que.append((nx, ny))
                        visited = [[0 for _ in range(w)] for _ in range(h)] # 새로운 키를 발견하면 방문처리 초기화!!!!
                        for a, b in entrance : 
                            que.append((a, b))
                    else : 
                        que.append((nx, ny))
                        visited[nx][ny] = 1
    
    # 3. 열쇠 다 먹은 상태로 돌아다니며 문서 찾기
    # 빈칸이나, 소문자면 그냥 큐에 달고
    # 대문자면, 키에 소문자 있을 때 큐에 달고
    # 문서이면, 카운트 +=1 하고 큐에 달기 
    # 방문기록은 그냥 바이너리로 0/1
    visited = [[0 for _ in range(w)] for _ in range(h)]
    for i, j in entrance : 
        que.append((i, j))
        visited[i][j] = 1

    while que : 
        x, y = que.popleft()
        if board[x][y].isupper() and board[x][y].lower() not in init_key : continue
        for i in range(4) : 
            nx, ny = x + dx[i], y + dy[i]
            if 0<= nx < h and 0 <= ny < w and not visited[nx][ny]:
                string = board[nx][ny]
                if string == '*' : continue
                if string == '$' : 
                    result += 1
                    que.append((nx, ny))
                    visited[nx][ny] = 1
                    continue
                
                if string == '.' or string.islower(): 
                    que.append((nx, ny))
                    visited[nx][ny] = 1
                    continue

                if string.isupper() :
                    if string.lower() not in init_key : continue
                    else : 
                        que.append((nx, ny))
                        visited[nx][ny] = 1
    
    print(result)
