# 사탕 게임

# 가장 처음에 N×N크기에 사탕을 채워 놓는다. 사탕의 색은 모두 같지 않을 수도 있다. 
# 상근이는 사탕의 색이 다른 인접한 두 칸을 고른다. 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다. 
# 이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.

# 사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성
# 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y

# 입력:
# CCP
# CCP
# PPC
# 출력: 3

# 브루트포스니까 -> 그냥 for문으로 구현
# 전체 입력 받기
# 첫번째 (0,0)부터 탐색 시작
# 1. 자신의 오른쪽, 아래쪽이 자신과 다른 문자라면 두 개 스위치 이후, 연속 사탕 카운트
    # 1-1) 인접(오른쪽, 아래쪽) 문자가 자신과 다른 문자인지 판별
        # 다른 문자라면 스왑 이후 아래 수행
    # 1-2) 연속 사탕 카운트 
        # 방금 바꾼 두개의 문자에 대해서만 카운트 <-- 바꾼거에 대해서만 해서는 안될 것 같다. 
        # 이미 안바꿔도 최대 길이 일 수도 있으니까 <-- 전체 다 
        # 그 카운트를 어떻게 하냐
            # max1(행에 대해서 카운트, 열에 대해서 카운트) <- Y
            # max2(행에 대해서 카운트, 열에 대해서 카운트) <- C
            # 최종 max(max1, max2)
            
# 2. 다시 배열 원본으로 초기화 <- 다시 스위치 하는걸로
# 3. i-1, j-1까지 반복 후 사탕의 최대 갯수 출력

# 시간초과 .. 안해
import sys
input = sys.stdin.readline

N = int(input())
candy = [list(map(str, input())) for _ in range(N)]

def count_candy(string) : # 해당 문자에 대한 최대 연속 길이 카운트 <- 이거 로직 다시 생각
    max_row = -1
    max_col = -1
    for i in range(N) :
        row = 0
        for j in range(N) :
            if candy[i][j] == string :
                if row == 0 : row += 1
                elif candy[i][j-1] == string : row += 1
        if max_row < row : max_row = row
        
    for i in range(N) :
        col = 0
        for j in range(N) :
            if candy[j][i] == string :
                if j == 0 : col = 1
                elif candy[j-1][i] == string : col += 1
        if max_col < col : max_col = col
    
    return max(max_row, max_col)
            
            
dx = [0, 1] # 우 하
dy = [1, 0] 
    
max_candy = -1
temp = 0
for i in range(N) :
    for j in range(N) :
        for k in range(2) : 
            nx = i + dx[k]
            ny = j + dy[k]
            
            if nx >= N or ny >= N: # 경계 넘어간 경우
                continue
            temp = max(count_candy('C'), count_candy('P'), count_candy('Z'), count_candy('Y'))
            if max_candy < temp : max_candy = temp
            if max_candy == N : break
            if candy[i][j] == candy[nx][ny] : continue
            # 다를 때
            candy1 = candy[i][j]
            candy2 = candy[nx][ny]
            # print("candy1: ", candy1, "candy2: ", candy2)
            candy[i][j], candy[nx][ny] = candy2, candy1 # swap
            # if candy1 == 'C' and candy2 == 'Y' :
            temp = max(count_candy(candy1), count_candy(candy2))
            if max_candy < temp : max_candy = temp
            candy[i][j], candy[nx][ny] = candy1, candy2 # 다시 복귀

print(max_candy)