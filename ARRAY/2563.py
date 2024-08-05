# 2차원 배열

# 가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다. 
# 이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다. 
# 이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 
# 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하시오.

# 예제 
# N (총 색종이의 수)
# a b () ... N만큼 반복
# a: 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리
# b: 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리

# a, b 최대 만큼 도화지 크기 다시 설정
# 도화지 만큼(100,100) 배열 만들어서 탐색하면 1로, 검은 영역 아니면 그대로 0으로 만들어서 마지막에 1값 다 더하기

import sys
input = sys.stdin.readline
rect = [[0 for _ in range(100)] for _ in range(100)] # 도화지 새로 초기화 (안 / 밖)

N = int(input())
count = 0
for _ in range(N) :
    a, b = map(int, input().split()) 
 
    temp_b = b
    for _ in range(10):
        b = temp_b
        for _ in range(10) :
            if rect[a][b] == 0 :
                rect[a][b] = 1
                count += 1
            b += 1
        a += 1

print(count)