# 마법사 상어와 파이어볼

# 기본적인 배열 사용 로직
    # arr 배열에 처음 공을 입력 받는다
    # arr 배열에서 꺼내서 fireball 삼차원 배열에 이동한 좌표와 값을 넣는다
        # 이 때 여기서는 비어있는 3차원 리스트로 같은 좌표에 공이 여러개 들어있는 것을 관리한다
    # fireball에서 모두 꺼내며, 1개 또는 4개로 변환한 좌표를 다시 arr에 넣는다
    # 즉 좌표 이동이 arr -> fireball -> arr 임 (이동시엔 당연히 비워야 하고)

# fireball 이라는 비어있는 3차원 리스트 생성
# 0. 입력 받을 때 좌표는 하나씩 -1해서 배열 arr에 추가
# 1. 모든 파이어볼 이동하기
    # 이동한 좌표로 fireball 추가 (arr에서 하나씩 꺼내면서)
        # nr, nc 계산
        # fireball[nr][nc].append([m, s, d]) 이런식으로 추가
# 2. fireball[nr][nc]의 길이 확인으로 2개 이상인지, 1개인지 확인
    # 공이 2개 이상이면 아래를 수행
        # 2-1. 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
            # 즉, 하나씩 꺼내며 m,s,d 에 추가 한다 (이 때 공 갯수도 세줘야 함)
                # 이 때 d는 %2 한걸로 더한다
        # 2-2. 파이어볼은 4개의 파이어볼로 나누어진다.
            # m, s, d 각각 계산한다.
                # d 같은 경우는 합이 0이거나 카운트와 같으면 짝수들로 / 아니면 홀수들로 추가
        # 2-3. arr에 4개 추가한다.
            # m // 5 가 0이 아니면, 좌표와 함께 m,s,d를 4번 append한다.
    # 공이 1개이면 그냥 fireball에서 꺼내서 arr에 추가

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())

arr = [] # r, c, m, s, d
for _ in range(M) : 
    r, c, m, s, d = map(int, input().split())
    arr.append([r-1, c-1, m, s, d])

fireball = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(K) :
    # 1. 이동 시키기 <- 이 때, arr에서 빼면서 비워둬야 함 (나중에 채울거니까)
    while arr : # 이동 시키기 
        r, c, m, s, d = arr.pop()
        nr = (r + s*dx[d]) % N
        nc = (c + s*dy[d]) % N
        fireball[nr][nc].append([m, s, d])
    
    # 2. 같은 자리에 공 2개 이상이면 4개로 만들기 // 1개면 그대로 추가
    for r in range(N) :
        for c in range(N) :
            if len(fireball[r][c]) >= 2 : 
                cnt, sum_m, sum_s, sum_d = 0, 0, 0, 0
                while fireball[r][c]: 
                    tmp_m, tmp_s, tmp_d = fireball[r][c].pop()
                    sum_m += tmp_m
                    sum_s += tmp_s
                    sum_d += tmp_d % 2
                    cnt += 1
                
                if sum_m // 5 : 
                    if sum_d == 0 or sum_d == cnt : tmp_d = 0
                    else : tmp_d = 1
                    for _ in range(4) :
                        arr.append([r, c, sum_m//5, sum_s//cnt, tmp_d])
                        tmp_d += 2
            elif len(fireball[r][c]) == 1 : 
                tmp_m, tmp_s, tmp_d = fireball[r][c].pop()
                arr.append([r, c, tmp_m, tmp_s, tmp_d])

print(sum(i[2] for i in arr))