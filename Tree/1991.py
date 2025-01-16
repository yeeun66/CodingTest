# 트리 순회
# 이진 트리를 입력받아 preorder, inorder, ostorder traversal한 결과를 출력하는 프로그램을 작성
# 자신(루트) - 왼 - 오 // 왼 - 자신(루트) - 오 // 왼 - 오 - 자신(루트)

# 첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다
# 파이썬으로 트리 구현하는 법을 아직 모르기 때문에 공부부터 한다! => 다했다!

# 방법
# 1. 트리 구현 (딕셔너리 사용)
# 2. 3가지 트래버셜 구현 (재귀 사용)
    # 재귀 호출시 순서 고려!
    # 재귀할 때 마다 함수 안의 ~~order(tree[root][0]) 재귀함수는 왼쪽으로 끝까지 탐색한다는 의미
    # 루트시에는 출력하면 됨

import sys
input = sys.stdin.readline

N = int(input())
tree = {} # 딕셔너리 선언
for _ in range(N) : # 트리 구현
    root, left, right = input().split()
    tree[root] = [left, right]

def preorder(root) : 
    if root != "." :
        print(root, end='') # 루트
        preorder(tree[root][0]) # 왼
        preorder(tree[root][1]) # 오

def inorder(root) : 
    if root != "." :
        inorder(tree[root][0]) # 왼
        print(root, end='') # 루트
        inorder(tree[root][1]) # 오

def postorder(root) : 
    if root != "." :
        postorder(tree[root][0]) # 왼
        postorder(tree[root][1]) # 오
        print(root, end='') # 루트

preorder('A')
print()
inorder('A')
print()
postorder('A')