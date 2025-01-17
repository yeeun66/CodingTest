# 완전 이진 트리
# 문제 조건을 보니 inorder 트래버셜 결과가 입력이고, 이 입력을 가지고 트리를 구성하면 될 듯
# 깊이가 K인 완전 이진 트리는 총 2^K-1개의 노드로 이루어져 있다 => 총 노드수 힌트
# 상근이가 종이에 적은 순서가 모두 주어졌을 때, 각 레벨에 있는 빌딩의 번호를 구하는 프로그램을 작성 (루트부터 출력)

# 재귀 호출
# 입력이 아래와 같을 때, 가장 가운데가 root이고, 이후 양 옆을 나눴을 때 가장 가운데가 다시 root이고, .. 이런식이기 때문에
# 센터를 찾고 양 옆으로 다시 재귀 탐색하며 각 level의 node를 업데이트 하면 됨
# 3
# 1 6 4 3 5 2 7

import sys
input = sys.stdin.readline
K = int(input())
arr = list(map(int, input().split()))

tree = [[] for _ in range(K)] # level별로 노드 저장할 배열

def make_tree(start, end, level) :
    if start == end : 
        tree[level].append(arr[start])
        return
    center = (start + end) // 2
    tree[level].append(arr[center])
    make_tree(start, center-1, level+1)
    make_tree(center+1, end, level+1)

make_tree(0, len(arr)-1, 0)

for t in tree : print(*t)