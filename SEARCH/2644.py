# 촌수 계산 (bfs 최단 거리 문제)

# 여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성
# 사람들은 1, 2, 3, …, n (1 ≤ n ≤ 100)의 연속된 번호로 각각 표시된다. 
# 첫째 줄에는 전체 사람의 수 n이 주어짐 (노드 수)
# 둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람의 번호가 주어짐 (탐색 해야 할 번호 => 시작 노드, 도착 노드)
# 그리고 셋째 줄에는 부모 자식들 간의 관계의 개수 m이 주어짐 (엣지 수)
# 넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x,y가 각 줄에 나온다. (엣지 관계)
# 이때 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호를 나타낸다. (d앵방향 그래프)

# 각 사람의 부모는 최대 한 명만 주어진다.
# 입력에서 요구한 두 사람의 촌수를 나타내는 정수를 출력한다. 
# 어떤 경우에는 두 사람의 친척 관계가 전혀 없어 촌수를 계산할 수 없을 때가 있다. 이때에는 -1을 출력

# 알고리즘 1) 시작노드와 도착노드 사이의 거리를 visit로 탐색(bfs) 후 출력. 각 노드에 최단거리 값 저장 --> result

from collections import deque
import sys

def bfs() :
    visit = [0] * (n+1)

    queue = deque([start])
    result[start] = 0
    visit[start] = True

    while queue :
        cur = queue.popleft()
        for i in graph[cur] :
            if not visit[i] :
                queue.append(i)
                visit[i] = True
                result[i] = result[cur] + 1

input = sys.stdin.readline

n = int(input())
start, end = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m) :
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

result = [-1] * (n+1)
bfs()
print(result[end])