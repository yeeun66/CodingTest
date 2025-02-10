# 이것이 코딩테스트다 책 - Ch4 구현 예제 1-01번) 상하좌우

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0] # L, R, U, D

N = int(input())
cmd = list(map(str, input().split()))

x, y = 1, 1
for c in cmd :
    if c == 'L' : i = 0
    elif c == 'R' : i = 1
    elif c == 'U' : i = 2
    elif c == 'D' : i = 3

    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 1 or nx > N or ny < 1 or ny > N : continue

    x, y = nx, ny

print(x, y)

    