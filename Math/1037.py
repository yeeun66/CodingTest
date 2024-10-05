# 약수
# 양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다
# 어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성

# 규칙을 보아하니 N은 주어진 수의 가장 작은수 x 가장 큰 수 인듯

a = int(input())
arr = list(map(int, input().split()))

max_num = max(arr)
min_num = min(arr)

print(max_num*min_num)