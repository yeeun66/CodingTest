# N과 M (11) - 백트래킹 연습
# M개 고르기. 중복 수열 불가 - set으로 안에 있는지 체크 
# 근데 이제 같은 수열 여러번은 가능

# 출력리스트에 담아뒀다가 한번에 출력
# 오름차순 정렬

N, M = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()

check = set() # 시간초과 이슈로 set으로 not in 검사 
output = []
def backtrack() :
    if len(arr) == M : 
        item = tuple(arr)
        if item not in check : 
            check.add(item)
            output.append(arr[:])

        return
    
    for i in range(0, N) :
        arr.append(n_list[i])
        backtrack()
        arr.pop()
            
arr = []
backtrack()

output.sort()
for o in output : print(*o)