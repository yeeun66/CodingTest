# 구간 합 구하기 5 (누적합 / DP)
# N×N개의 수가 N×N 크기의 표에 채워져 있다. (x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램을 작성 (행, 열)

# 이차원 리스트 입력 받고 이것들의 누적합 리스트 따로 만들기 <DP 이용>
#   리스트 채우는 법: 구하고자 하는 자리에 (i-1 누적합) + (j-1 누적합) - (중복 영역 = 대각선 i-1,j-1) + 원래 (i, j) 값

# 입력 받은 좌표 (정수4개)에 대하여 누적합 연산 후 출력
#   연산 방법: (x2, y2) - (x2, y1-1) - (x1-1, y2) + (x1-1, y1-1)

# - notion에 그림으로 정리해놓음
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = []
for _ in range(N) :
    arr.append(list(map(int, input().split())))

sum_list = [[0] * (N+1) for _ in range(N+1)]

# 누적합 리스트 만들기
for i in range(1, N+1) :
    for j in range(1, N+1) :
        if i == 1 and j ==1 : sum_list[i][j] = arr[0][0]
        elif i == 1 :
            sum_list[i][j] = arr[i-1][j-1] + sum_list[i][j-1]
        elif j == 1 :
            sum_list[i][j] = arr[i-1][j-1] + sum_list[i-1][j]
        else : sum_list[i][j] = arr[i-1][j-1] + sum_list[i][j-1] + sum_list[i-1][j]  - sum_list[i-1][j-1]
        
# 구간합 구하기 
for _ in range(M) : 
    x1, y1, x2, y2 = map(int, input().split())
    print(sum_list[x2][y2] - sum_list[x1-1][y2] - sum_list[x2][y1-1] + sum_list[x1-1][y1-1])