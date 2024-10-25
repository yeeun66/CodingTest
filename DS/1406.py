# 에디터
# 초기에 편집기에 입력되어 있는 문자열이 주어지고, 그 이후 입력한 명령어가 차례로 주어졌을 때, 
# 모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 구하는 프로그램

# 편집기가 지원하는 명령어
# L: 커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
# D: 커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
# B: 커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
    # 삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
# P $: $라는 문자를 커서 왼쪽에 추가함

# 시간 초과 해결 - 문자 합치기, insert, del, [0:] 이런거 썼다간 시간 복잡도 겁나 큼
# 해결법 -> 커서는 그대로 둔 채 커서 기준 좌측, 우측 리스트에 문자를 입력하는 방식
    
from collections import deque
import sys
input = sys.stdin.readline

left = list(input().strip())
right = deque()

M = int(input())  # 명령어 갯수

for _ in range(M):
    cmd = input().strip()
    
    if cmd[0] == 'L' and left:
        right.appendleft(left.pop())
    elif cmd[0] == 'D' and right:
        left.append(right.popleft())
    elif cmd[0] == 'B' and left:
        left.pop()
    elif cmd[0] == 'P':
        left.append(cmd[2])  # P X 명령에서 X 문자를 추가

# left와 right 스택을 합쳐 출력
print(''.join(left) + ''.join(right))