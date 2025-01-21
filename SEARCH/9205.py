# 맥주 마시면서 걸어가기

# 출발은 상근이네 집에서 하고, 맥주 한 박스를 들고 출발한다. 맥주 한 박스에는 맥주가 20개 들어있다.
# 50미터를 가려면 그 직전에 맥주 한 병을 마셔야 한다. 
# 맥주를 편의점에서 더 구매해야 할 수도 있다. 
# 편의점에 들렸을 때, 빈 병은 버리고 새 맥주 병을 살 수 있다. 하지만, 박스에 들어있는 맥주는 20병을 넘을 수 없다. 
# 편의점을 나선 직후에도 50미터를 가기 전에 맥주 한 병을 마셔야 한다.

# 입력: 
    # 각 테스트 케이스의 첫째 줄에는 맥주를 파는 편의점의 개수 n이 주어진다. (0 ≤ n ≤ 100).
    # 다음 n+2개 줄에는 상근이네 집, 편의점, 펜타포트 락 페스티벌 좌표가 주어진다. 
    # 각 좌표는 두 정수 x와 y로 이루어져 있다. (두 값 모두 미터, -32768 ≤ x, y ≤ 32767) 
        # <= 배열 음수로 인덱스 할 수 없으니까 모든 좌표에 + 32768 해주기
    # 송도는 직사각형 모양으로 생긴 도시이다. 두 좌표 사이의 거리는 x 좌표의 차이 + y 좌표의 차이 이다. (맨해튼 거리)
# 출력: 상근이와 친구들이 행복하게 페스티벌에 갈 수 있으면 "happy", 중간에 맥주가 바닥나서 더 이동할 수 없으면 "sad"

# 방법1: => 메모리 너무 많이 차지해서 코드 실행이 안됨 (1미터씩 탐색하며 맥주 줄면 충전하고 그런 방식)

# 방법 2 (거리 사용, bfs인 이유가 있었다!) 
# 출발, 도착 위치 따로 입력 받음. 편의점 좌표들은 따로 배열에 입력 받음
# 출발 위치를 queue에 넣는다
    # bfs탐색 : queue에서 하나씩 popleft 하며 다음을 반복
        # 방금 pop한 좌표와 dst 좌표의 거리가 1000 이하면, 리턴 happy
        # 아니면 아래 수행
        # 방금 pop한 좌표와의 거리가 1000 이하인 좌표를 모두 큐에 넣고 배열에서는 지운다.
            # 이때 큐에 추가되는 좌표들이 인접노드들이다 (1000이하로 갈 수 있는 모든 곳)
    # 반복문 탈출 후 sad 리턴

import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, a, b) :
    queue = deque()
    queue.append((x, y))

    while queue :
        x, y = queue.popleft() 
        tmp = abs(a-x) + abs(b-y)
        if tmp <= 1000 : return 'happy'
        for i in range(len(arr)) :
            if i < len(arr) :
                n = arr[i][0]
                m = arr[i][1]
                tmp = abs(x-n) + abs(y-m)
                if tmp <= 1000 :
                    queue.append((n, m))
                    del arr[i]
        
    return 'sad'
    

T = int(input())

for _ in range(T) :
    arr = []
    c = int(input())
    x, y = map(int, input().split()) # src
    for _ in range(c) : # 편의점 위치 보관
        a, b = map(int, input().split())
        arr.append((a, b))
    a, b = map(int, input().split()) # dst
    print(bfs(x, y, a, b))