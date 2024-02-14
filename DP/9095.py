# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램

# 첫째 줄에 테스트 케이스의 개수 T

T = int(input())

# 답들을 저장할 리스트
a = [0] * 11

a[1] = 1
a[2] = 2
a[3] = 4

for i in range(4, 11) : 
    a[i] = a[i-1] + a[i-2] + a[i-3] 

for _ in range(T) : 
    test = int(input())
    print(a[test])