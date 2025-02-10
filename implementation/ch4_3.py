# 이것이 코딩테스트다 책 - Ch4 구현 예제 02번) 왕실의 나이트 

# 상하좌우 문제와 유사, but 4가지 말고 L자로 이동하여 총 8가지 경우의 수가 나오게 됨
    # 이때 입력 위치에서 8가지 경우에 대해 범위에 벗어나지 않으면 cnt += 1 하면 됨

dx = [-2, -2, 2, 2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]

init = input()
col, row  = init[0], int(init[1])

col = ord(col) - ord('a') + 1

cnt = 0
for i in range(8) :
    nx = col + dx[i]
    ny = row + dy[i]

    if nx < 1 or nx > 8 or ny < 1 or ny > 8 : continue
    cnt += 1
print(cnt)