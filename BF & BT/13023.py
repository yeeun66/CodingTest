# ABCDE
# 양방향 그래프 딕셔너리에 넣으면 되지 않나?
# 친구관계 연속 5개 만족하면 성공
"""
로직 
양방향 그래프에 넣어 관리

백트래킹인데 이제 조건
1. 배열 길이 5이상이면 1출력 후 그냥 종료
2. 재귀 매달 때, 현재 값에 연결된 값들만 매달기
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M) : 
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def backtrack() :
    if len(arr) >= 5 :
        print(1)
        exit()

    last = arr[-1] 
    for n in graph[last] :
        if n in arr : continue
        arr.append(n)
        backtrack()
        arr.pop()

arr = []
for i in range(N):
    arr.append(i)
    backtrack() # 0~N-1은 밖에서 반복
    arr.pop()

print(0)