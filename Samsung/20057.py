# 마법사 상어와 토네이도

# 배열 회전 알고리즘 블로그 참고함 ** 중요하니까 암기
    # 90도 회전: ret[4-j][i] = ratio[i][j] # 왼쪽이 회전 후
        # 이전 행 => 현재 열
        # (N-1) - 이전 열 => 현재 행

# 0. 초기 작업
    # 좌, 하, 우, 상 (토네이도 방향) 배열 하나에 저장 
    # ratio 배열 0으로 초기화 후 해당 비율 실수로 저장 (알파는 -1로 두기)
# 1. 입력 받기, 배열 생성
    # send 배열에 모래 양 입력 받기
    # result 변수에 격자 빠져나간 모래 저장하기
# 2. 토네이도 시전
# r, c = (N-1)/2, (N-1)/2 부터 시작 => (1, 1)될 때 까지 아래 반복
    # 2-1. 토네이도 이동
        # 토네이도 방향 교체 
            # s는 계속 1씩 증가
            # 처음엔 1일 때 2번 방향 변경, 다음엔 2일 때 방향 2번 변경 이런식으로 (idx, count, s 사용)
            # 따라서 s == idx 방향 d 1 증가 후 d = (d + 4) % 4 
        # d 이용하여 토네이도 한칸 씩 이동하기
            # nr = r + dx[d]
            # nc = c + dy[d]
    # 2-2. 토네이도가 이동한 위치에 대하여 모래 흩날리기
        # 현재 nr, nc와 (2, 2 <- ratio의 중심)의 차이를 구한다.
            # (tx, ty)라 하자.
        # 이중 반복(5*5)하며
            # ratio[i][j] == 0이면: 컨티뉴
            # ratio[i][j] == -1이면: a, b = i, j 저장하고 컨티뉴
            # 현재 위치 계산 ni = i + tx, nj = j + ty 하고
                # 더해줄 비율도 계산 send[r][c] * ratio[i][j]
                # 현재 위치(ni, nj)가 격자 밖이면, result에 더하고
                # 격자 내부이면, 현재 위치에 더함 
                # (공통) 누적합 sums에 방금 더한 것 더해주기
        # 알파 위치(a, b)에 남은 값 더해주기 (send[r][c] - sums)
        # 현재 모래는 send[r][c] = 0 초기화후 r, c = nr, nc로 초기화
# 2-3. ratio 배열 90도 회전시키기 (그리고 d+=1)
    # 이중 반복 하며, 0이 아닌 값에 대하여 
        # 이전 행 => 현재 열
        # 4 - 이전 열 => 현재 행
            # 비율 값을 업데이트 해주기
# 3. print(result)

dx = [0, 1, 0, -1] # 좌 하 우 상
dy = [-1, 0, 1, 0]
ratio = [[0] * 5 for _ in range(5)]
ratio[1][3], ratio[3][3] = 0.01, 0.01
ratio[0][2], ratio[4][2] = 0.02, 0.02
ratio[2][0], ratio[2][1] = 0.05, -1
ratio[1][2], ratio[3][2] = 0.07, 0.07
ratio[1][1], ratio[3][1] = 0.1, 0.1

def rotate_90(ratio): 
    ret = [[0]* 5 for _ in range(5)]
    for i in range(5) :
        for j in range(5) :
            ret[4-j][i] = ratio[i][j]
    
    return ret

N = int(input())
send = []
for _ in range(N) : send.append(list(map(int, input().split())))
result = 0

r, c = int((N-1)/2), int((N-1)/2)
d, s = 0, 0 # 방향, 칸수
idx, count = 1, 0
while(True) :

    nr, nc = int(r + dx[d]) , int(c + dy[d]) # 이동할 곳의 좌표
    tx, ty = nr - 2, nc -2 # 모래 배열에 비율 배열을 포개기

    sums = 0
    for i in range(5) :
        for j in range(5) : 
            if ratio[i][j] == 0: continue
            elif ratio[i][j] == -1: a, b = i + tx, j + ty
            else : 
                ni, nj = i + tx, j + ty # 현재 모래 배열에서의 위치
                tmp = int(send[nr][nc] * ratio[i][j])
                if 0 <= ni < N and 0 <= nj < N : send[ni][nj] += tmp
                else : result += tmp
                sums += tmp
    remain = send[nr][nc] - sums # 알파값 처리 

    if 0 <= a < N and 0 <= b < N : send[a][b] += remain
    else : result += remain

    send[nr][nc] = 0
    r, c = nr, nc
    
    # 토네이도 방향 교체 
    s += 1
    if s == idx : # 현재 idx칸 만큼 이동했으면, 방향 바꾸고, 비율 배열도 회전하고, 
        # 다시 s=0으로 바꿔서 다시 칸수 세기
        d += 1
        d = (d + 4) % 4 
        s = 0
        count += 1
        ratio = rotate_90(ratio) # 90도 회전 
    
    if count == 2 : # 현재 방향으로 idx칸 만큼 이동은 두번씩만
        idx += 1 
        count = 0

    if r == 0 and c == 0: continue
    if r <= 0 and c <= 0 : break

print(result)