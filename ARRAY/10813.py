# 공바꾸기2 (10810 업그레이드 버전)
# 도현이는 공을 바꿀 바구니 2개를 선택하고, 두 바구니에 들어있는 공을 서로 교환한다.
# 바구니에는 공이 1개씩 들어있고, 처음에는 바구니에 적혀있는 번호와 같은 번호가 적힌 공이 들어있다.
# 공을 어떻게 바꿀지가 주어졌을 때, M번 공을 바꾼 이후에 각 바구니에 어떤 공이 들어있는지 구하는 프로그램을 작성

# 입력 예시
# N, M
# i, j 
# ... (M 만큼)

# 코드 생각하고 써...

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = [i+1 for i in range(N)] # 1, 2, 3, .. N 때려 넣어

for _ in range(M) : 
    i, j = map(int, input().split())
    a[i-1], a[j-1] = a[j-1], a[i-1]

print(*a)