# 테트로미노
# 테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 작성
# 핵심 아이디어: 이 문제를 보고 'ㅗ'를 제외한 나머지 블록은 dfs로 구할 수 있다는 것 캐치, 
#            그리고 'ㅗ'는 상하좌우만 보면 된다는점 캐치
# 했으면 거의 성공.. ('ㅗ' 모양 제외 나머지는 시작점 부터 선 하나로 탐색 가능)

# 로직
# 1. 입력 받기 (배열은 graph 배열에 저장)
# 2. 이중 for문으로 방문하지 않은 좌표에 대해, dfs방문 ('ㅗ' 제외 다른 블록들)
    # dfs 탐색. dfs(i, j, graph[i][j], cnt) <- 3번째 파라미터는 누적합
        # 2-1. cnt가 4개가 되면 maximum값 업데이트 후 리턴
        # 2-2. 현재 위치에서 상하좌우 탐색
            # 탐색하면서, 방문 전이면 방문 처리 후, dfs 호출 (재귀)
                # 이때 dfs 호출하면서 cnt 증가 시키기
            # 방문 끝나면 (dfs return 되면) 방문 취소

# 3. 2와 같은 for문에서 'ㅗ' 모양 탐색 함수 호출
    # find_oh(i, j, graph[i][j])
        # 현재 위치에서 상하좌우 탐색하면서 arr 배열에 값들 추가
            # arr 배열에 추가된 갯수가 4개이면
                # 그 중 가장 작은거 삭제 후, 현재값과 더하면 ㅗ 모양이 됨
            # arr의 갯수가 3개이면, ㅗ 모양 완성이므로 현재값과 바로 더하면 됨
            # 2개 이하이면, 그냥 return
# 4. 두 함수를 모두 다녀온 좌표에 대해 다시 방문 취소 처리 (그래야 나중에 다른 좌표에 의해 방문됨)

N, M = map(int, input().split())

graph = []
for _ in range(N) : graph.append(list(map(int, input().split())))

visited = [[False] * M for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
maximum = 0

def dfs(x, y, tmp, cnt): # dfs로 모두 탐색
    global maximum
    if cnt == 4 : 
        maximum = max(maximum, tmp)
        return
    
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] :
            visited[nx][ny] = True
            dfs(nx, ny, tmp + graph[nx][ny], cnt +1)
            visited[nx][ny] = False

def find_oh(x, y, tmp) : # 'ㅗ' 블록 따로 구하기
    global maximum
    arr = []
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] :
            arr.append(graph[nx][ny])
    
    length = len(arr)
    if length == 4 : 
        arr.sort(reverse=True) # 내림차순
        arr.pop() # 가장 작은거 pop
        maximum = max(maximum, sum(arr) + tmp)
    elif length == 3 : maximum = max(maximum, sum(arr) + tmp)
    else: return

for i in range(N) :
    for j in range(M) :
        visited[i][j] = True
        dfs(i, j, graph[i][j], 1)
        find_oh(i, j, graph[i][j])
        visited[i][j] = False

print(maximum)