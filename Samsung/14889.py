# 스타트와 링크 (백트래킹.. 어렵다)
# 바로 조합이 떠오르지만.. 일단 백트래킹으로 풀어보자 (다른 분 풀이 참고)

# 1. status 입력 받기 
# 2. 결과 값 최대로 초기화 (result)
# 3. DFS 수행
    # 3-1. dfs(depth, idx) 로 설정
        # depth는 확정된 선수의 수, idx는 다음으로 고려할 선수의 인덱스
    # 3-2. (0,0)부터 시작
    # 3-3. depth == N/2 가 되면
        # 스타트팀과 링크팀의 능력치 0으로 초기화
        # 현재 방문된 선수를 스타트 팀이라 하고, 방문되었으면, 스타트팀에 능력치 더함
        # 방문 안했으면, 링크 팀에 능력치 더함
        # result에 스타트-링크 팀 차이 최소로 업데이트
    # 3-4. 아직 절반 구성 못했으면
        # 팀원을 구성한다 -> 이때 백트래킹!
        # 반복문 idx부터 N까지
            # 아직 방문하지 않았다면, 
                # 방문 표시 후, 
                # dfs(depth + 1, i + 1) -> 팀원 수 증가, 다음선수 인덱스로 증가
                # 이후 방문 표시 삭제

N = int(input())
status = [list(map(int, input().split())) for _ in range(N)]

result = (200 * N * N) + 1
visited = [False] * N

def dfs(depth, idx) :
    global result
    
    if depth == N // 2 :
        
        start = 0
        link = 0
        
        for i in range(N) :
            for j in range(N) :
                
                if visited[i] and visited[j] : # 둘다 방문 했으면
                    start += status[i][j]
                elif not visited[i] and not visited[j] : # 둘다 방문 안했으면
                    link += status[i][j]
        
        result = min(result, abs(start-link))
        return
    
    else :
        for i in range(idx, N) : # 이전에 선택한 선수 선택하지 않도록 idx부터 
            if not visited[i] : 
                visited[i] = True # 현재 선수 포함 시키고
                dfs(depth+1, i+1) # 구성원 +1, 다음 선수로 인덱스 증가
                visited[i] = False # 현재 선수 제외 시켜

dfs(0, 0)
print(result)