# N과 M (10) - 백트래킹 연습
# M개 고르기. 중복 불가(방문기록으로 중복 체크)
# 비내림차순이어야 함. 즉 오른쪽이 왼쪽보다 커서는 안됨

# 출력리스트에 담아뒀다가 한번에 출력
# 오름차순 정렬

N, M = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()

output = set() # 시간초과 이슈로 set으로 not in 검사 
visited = [False] * N

def backtrack() :
    if len(arr) == M : 
        item = tuple(arr)
        if item not in output : 
            output.add(item)
        return
    
    for i in range(0, N) :
        if not arr and not visited[i]:
            visited[i] = True
            arr.append(n_list[i])
            backtrack()
            arr.pop()
            visited[i] = False # 빼고 나서는 다시 방문기록 복귀
            
        elif not visited[i] and n_list[i] >= arr[-1]:
            visited[i] = True
            arr.append(n_list[i])
            backtrack()
            arr.pop()
            visited[i] = False # 빼고 나서는 다시 방문기록 복귀

arr = []
backtrack()

output = list(output)
output.sort()
for o in output : print(*o)