# 연속합

# n개의 정수로 이루어진 임의의 수열이 주어진다. 
# 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다. 
# 단, 수는 한 개 이상 선택해야 한다.
# 예를 들어서 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 이라는 수열이 주어졌다고 하자. 
# 여기서 정답은 12+21인 33이 정답이 된다.

# 누적합 논리 (이게 되네??)
# 1. 각 인덱스 마다 현재까지의 합인 누적합을 모두 구한다 (배열 sum[])
# 2. 누적합 구하면서 동시에 이전까지의 최소 누적합을 업데이트 한다 (배열 small[]) 이때 0번째 배열에는 0을 넣는다
# 3. 각 인덱스 마다 (누적합 - 최소 누적합) 과 그냥 누적합 중 큰 값을 선택하여 결과 에 저장 (원래 배열 arr[])
# 4. 결과 배열(arr) 값 중 최대 값을 출력 

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
sum = [0] * n
small = [1001] * n
small[0] = 1
tmp = 0
for i in range(n) :
    tmp += arr[i]
    sum[i] = tmp
    if i != 0 : small[i] = min(small[i-1], sum[i-1])
    arr[i] = max(sum[i], sum[i]-small[i])
print(max(arr))