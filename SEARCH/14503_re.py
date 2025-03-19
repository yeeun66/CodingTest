# 로봇 청소기와 방의 상태가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램을 작성
# 1. 방 크기, (처음 좌표, 방향), 전체 상태 입력 받기
# 2. 동서 남북 방향 배열 지정
# 3. 처음 좌표부터 시작해서, 다음을 반복
    # 3-1. 현재 칸이 0인 경우) 현재 칸 2로 바꾼다
    # 3-2. 현재 칸의 주변 4칸 탐색하며 (반시계 방향으로 90도씩 회전)
        # 이 때 원래 방향 저장해둘 필요 있음
        # 90도 회전 후 앞칸이 0인 경우 (0인 경우)
            # 한칸 전진하고 3-1번으로 돌아간다
        # 0이 없는 경우,
            # 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 3-1번으로 돌아간다
            # 바라보는 방향의 뒤쪽 칸이 1이라 후진 불가하면 작동 멈춘다
# 4. 배열에서 청소된 칸, 즉 값이 2인 갯수 출력 (2차원 배열이라 반복문으로 세야 함)

# 상태 점검 >> 1: 벽 / 0: 청소되지 않은 칸 / 2: 청소된 칸

N, M = map(int, input().split())
r, c, d = map(int, input().split())

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

arr = []

for i in range(N) :
    arr.append(list(map(int, input().split())))

stop = 0 # 중단 여부
while True : 
    if stop : break
    if arr[r][c] == 0 : arr[r][c] = 2
    origin = d # 원래 방향 저장
    serach = 0 # 주변 0의 여부
    for i in range(4) : 
        d = (d+3) % 4 # 90도 회전 후 앞칸 
        nr = r + dx[d]
        nc = c + dy[d]
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0 : # 앞칸 이동 가능이면
            r, c = nr, nc 
            serach = 1
            break   
    if not serach : # 4방향 모두 0이 없는 경우
        d = (d+2) % 4 # 후진
        nr = r + dx[d]
        nc = c + dy[d]
        if nr < 0 or nr >= N or nc < 0 or nc >= M : # 범위 벗어나도 끝내
            stop = 1
        elif arr[nr][nc] == 1 : # 후진했을 때 벽이면
            stop = 1
        else : 
            r, c = nr, nc  
            d = origin # 방향 되돌리기

cnt = 0
for i in range(N) :
    cnt += arr[i].count(2)
print(cnt)