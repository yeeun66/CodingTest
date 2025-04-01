# 상어 초등학교
# 구현

# 1. 입력 받기
    # N 입력 받은 후 NxN 배열 arr 생성, 0으로 초기화
    # 이후 N^2 만큼 입력 받은후 2차원 배열 favorite에 저장
    # fav[0]은 현재 배정할 학생의 번호(나머지는 좋아하는 학생 번호)

# 2. 자리 배정 (favorite 순서대로 꺼내서 배정)

    # 1. 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
        # 현재 칸에 좋아하는 학생 존재 여부 구하기:
            # 이중 for문 돌면서 0이 아닌 값에 대하여 현재 favorite에 있는지 확인
                # 있다면, 해당 칸 주변 중 0인 칸 좌표 tmp1에 추가하고 그 주변칸 -1하기

        # 현재 칸에 좋아하는 학생이 없는 경우 (tmp배열이 empty인 경우)
            # 모든 빈칸 선택 후 tmp1.append(좌표)
                # 하나면 배정 끝 - 해당 좌표에 배정할 학생 넣기, continue
                # 여러 개면 2번으로 넘어감
        # 칸에 좋아하는 학생이 있는 경우
            # 빈칸 중 좋아하는 학생의 수가 많이 인접한 칸 선택 후
                # tmp1에서 가장 작은 값들만 tmp2로 이사 시키기
                    # 선택 칸이 하나면 배정 끝
                    # 여러개면 2번으로 넘어감 

    # 2. 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
        # 1번에서 담긴 칸들(tmp2) 중 인접한 칸이 가장 많은 칸 선택
            # 해당 칸에서 주변의 빈칸 수 탐색
                # 처음엔 tmp3에 그냥 추가, maxx 변수에 인접 갯수 업데이트
                    # 다음 칸이 앞에 칸보다 많으면, 있던거 다 빼고, 그거 추가하고 변수에 인접 갯수 업데이트
                    # 앞에 칸과 같으면 그냥 추가
                    # 작으면 skip
                # 선택 칸(tmp3)이 하나면 배정 끝
                # 여러개면 3번으로

    # 3. 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
        # tmp3 중 행 번호, 열 번호 작은 칸으로 선택 (sort) 
    # 4. arr에서 음수인 좌표들 모두 0으로 바꾸기 <- 이거 코드 초반 초기화 단계로 옮김

# 3. 만족도 총합 구하기 (딕셔너리 사용)
    # 자리 배치가 끝난 arr 배열에서 (0, 0) 위치 학생 부터, 
    #   현재 학생과 인접한 학생과 주변에 좋아하는 친구 수를 구한다.  
    #   친구 수에 따른 점수 result에 합산 (1이면 1, 2이면 10, 3이면 100, 4이면 1000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
arr = [[0] * N for _ in range(N)]

favorite = []
for _ in range(N**2) : favorite.append(list(map(int, input().split())))

for fav in favorite : 
    tmp1 = []
    tmp2 = []
    tmp3 = []
    # arr 다시 0으로 만들기
    for i in range(N) :
        for j in range(N) :
            if arr[i][j] < 0 : arr[i][j] = 0

    # 1번 
    for i in range(N) : 
        for j in range(N) :
            if arr[i][j] != 0 :     
                if arr[i][j] in fav : 
                    for k in range(4) :
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if 0<=nx<N and 0<=ny<N : 
                            if arr[nx][ny] == 0 : 
                                tmp1.append((nx, ny))
                                arr[nx][ny] -= 1
                            elif arr[nx][ny] < 0 : 
                                arr[nx][ny] -= 1
    if not tmp1 :
        for i in range(N) : 
            for j in range(N) :
                if arr[i][j] == 0 : 
                    tmp1.append((i, j)) 
        if len(tmp1) == 1 : 
            nx, ny = tmp1[0]
            arr[nx][ny] = fav[0]
            continue
        else: tmp2 = tmp1
    else : 
        mini = 0
        for t in tmp1 :
            nx, ny = t
            tmp = arr[nx][ny]
            mini = min(mini, tmp)
        
        for t in tmp1 :
            nx, ny = t
            tmp = arr[nx][ny]
            if tmp == mini : tmp2.append((nx, ny))
        
        if len(tmp2) == 1 : 
            nx, ny = tmp2[0]
            arr[nx][ny] = fav[0]
            continue
    # 2번
    maxx = 0
    for t in tmp2 : 
        cnt = 0
        x, y = t
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and arr[nx][ny] <= 0: cnt += 1
        if not tmp3: 
            tmp3.append((x, y))
            maxx = cnt
        else: 
            if maxx < cnt : 
                tmp3 = []
                tmp3.append((x, y))
                maxx = cnt
            elif maxx == cnt : tmp3.append((x, y))
    
    if len(tmp3) == 1 : 
        nx, ny = tmp3[0]
        arr[nx][ny] = fav[0]
        continue
    
    # 3번 
    tmp3.sort()
    if tmp3 : 
        nx, ny = tmp3[0]
        arr[nx][ny] = fav[0]
    
# 만족도 총합 구하기
dic = {}
for fav in favorite : dic[fav[0]] = fav[1], fav[2], fav[3], fav[4]

result = 0
for i in range(N) :
    for j in range(N) :
        key = arr[i][j]
        cnt = 0
        for k in range(4) : 
            nx = i + dx[k]
            ny = j + dy[k]
            if 0<=nx<N and 0<=ny<N : 
                if arr[nx][ny] in dic[key] : cnt += 1
        
        if cnt == 1 : result += 1
        elif cnt == 2 : result += 10
        elif cnt == 3 : result += 100
        elif cnt == 4 : result += 1000

print(result) 