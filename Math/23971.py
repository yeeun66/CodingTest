# table이 H행 W열
# 거리두기 수칙 => 모든 참가자는 세로로 N칸, 가로로 M칸 이상 비우고 앉아야 함
# 이 수칙을 지키면서 강의실이 최대 몇 명 수용할 수 있는지 구하기

# -- 메모리 초과 개오바 이게 왜 수학 문제 난 모르겠어 -- 
import sys
input = sys.stdin.readline

H, W, N, M = map(int, input().split())

# H by W 행렬 모두 0으로 초기화
# 값이 0인 곳 탐색
    # 이 위치를 2로 바꿈
    # 그 주변을 (i, j+M), (i+N, j), (i+N, j+M) 모두 -0(앉을 수 없는 자리)로 만듦
# 반복문 끝나면 배열에 있는 2의 갯수를 출력

table = [[0 for _ in range(W)] for _ in range(H)] # 안이 column, 밖이 row

for i in range(H) :
    for j in range(W) :
        if table[i][j] == 0 :
            table[i][j] = 2
            if j + M < W : 
                table[i][j+M] = -1
            if i + N < H : 
                table[i+N][j] = -1
            if j + M < W  and i + N < H :
                table[i+N][j+M] = -1

count = sum(row.count(2) for row in table)
print(count)