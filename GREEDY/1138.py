# 한 줄로 서기

# N명의 사람들은 매일 아침 한 줄로 선다. 이 사람들은 자리를 마음대로 서지 못하고 오민식의 지시대로 선다.
# 어느 날 사람들은 오민식이 사람들이 줄 서는 위치를 기록해 놓는다는 것을 알았다. 그리고 아침에 자기가 기록해 놓은 것과 사람들이 줄을 선 위치가 맞는지 확인한다.
# 사람들은 자기보다 큰 사람이 왼쪽에 몇 명 있었는지만을 기억한다. N명의 사람이 있고, 사람들의 키는 1부터 N까지 모두 다르다.
# 각 사람들이 기억하는 정보가 주어질 때, 줄을 어떻게 서야 하는지 출력하는 프로그램을 작성하시오.

# 첫째 줄에 사람의 수 N이 주어진다. N은 10보다 작거나 같은 자연수이다. 둘째 줄에는 키가 1인 사람부터 차례대로 자기보다 키가 큰 사람이 왼쪽에 몇 명이 있었는지 주어진다. 
# i번째 수는 0보다 크거나 같고, N-i보다 작거나 같다. i는 0부터 시작한다.

# 방법:
    # 크기 N의 배열을 모두 -1로 초기화 한다
    # n = 1부터 N까지 자신 인덱스의 있는 단서로 자신의 위치를 찾아간다
        # 우선 인덱스 0번 부터 안에 아직 값이 없으면 (즉 -1이면, 카운트를 한다)
        # 이 때 자신의 값이 0이면 -1을 만나자 마자 그곳을 자신으로 바꾸고 break 한다
        # 0이 아니라면 -1갯수를 카운트 하고 -1의 갯수가 자신의 갯수와 일치 하면 그 이후 반복문에서 -1 발견시 그곳에 넣는다

N = int(input())
arr = list(map(int, input().split()))
result = [-1] * N

for i in range(N) :
    cnt = 0  # 왼쪽의 -1 갯수
    value = i + 1
    for j in range(N) :
        if result[j] == -1 :
            if arr[i] == 0 : 
                result[j] = value
                break
            if cnt == arr[i] :  
                result[j] = value
                break
            else: cnt += 1

print(*result)