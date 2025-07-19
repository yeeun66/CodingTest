# 부분수열의 합
# N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램
# 백트래킹으로 모든 조합 구해서 합이 S가 되면 경우의 수 1 카운트 (전역 변수로 사용)

# 같은 수 여러번 사용X, 같은 수열 중복X --> idx로 이전 배열에는 접근x 한번에 해결 가능 

# vscode 에서도 시간 오래걸려서 안뜨는 문제 해결
    # 굳이 배열에 다 매달 필요가 없음. 왜? 원소 조합 출력하라고 안했잖아
    # 그럼 어떻게? sum 같은 경우의 수 찾으라 했으니까 순차적으로 sum만 하면 됨!

N, S = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()

cnt = 0

def backtrack(sums, depth, idx) : # 현재까지의 합과 깊이, 그리고 현재까지의 인덱스를 파라미터로 지정 
    global cnt

    if sums == S : cnt += 1

    if depth >= N : return

    for i in range(N) :
        if i > idx : # 중복 방지
            if sums == 1000001 : sums = 0
            sums += n_list[i]
            backtrack(sums, depth+1, i)
            sums -= n_list[i]

backtrack(1000001, 0, -1)
print(cnt)