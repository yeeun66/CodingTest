# 알파벳 블록을 일렬로 조립하여 문자열을 만드는 게임을 만들었다. 
# 각 블록에는 문자 하나가 적혀 있으며 게임에는 각각 다음 기능을 수행하는 세 개의 버튼이 있다.
        # 문자열 맨 뒤에 블록 추가
        # 문자열 맨 앞에 블록 추가
        # 문자열을 구성하는 블록 중 가장 나중에 추가된 블록 제거
# 게임은 처음에 빈 문자열로 시작하며 빈 문자열일 때 문자열을 구성하는 블록 중 가장 나중에 추가된 블록을 제거하는 버튼을 누를 경우 아무런 동작도 하지 않는다. 
# 버튼을 누른 횟수와 누른 버튼이 순서대로 주어질 때 완성된 문자열을 구하여라.

# 큐1 - 문자열 저장
# 큐2 - 명령어 1 또는 2 저장

import sys
from collections import deque

input = sys.stdin.readline

queue = deque()
cmd = []
N = int(input())

for _ in range(N) :
    parts = input().split() # list

    if parts[0] == '1' :
        queue.append(parts[1])
        cmd.append(1)
    elif parts[0] == '2' :
        queue.appendleft(parts[1])
        cmd.append(2)
    elif parts[0] == '3' :
        if queue and cmd :
            cmds =  cmd.pop() 
            if cmds == 1 :
                queue.pop()
            elif cmds == 2 :
                queue.popleft()

if not queue : print(0, end='')
else: print(''.join(queue), end='')