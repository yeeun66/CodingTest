# DS 탐색 (binary search)
# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 
# 상근이는 숫자 카드 N개를 가지고 있다. 
# 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

# 10 ==> 숫자 카드의 개수 N
# 6 3 2 10 10 10 -10 -10 7 3 => 숫자 카드에 적혀있는 정수
# 8 => 아래에 주어질 정수 M개
# 10 9 -5 2 3 4 5 -10 ==> 이 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.

import sys
input = sys.stdin.readline

N = int(input())
card = list(map(int, input().split()))
M = int(input())
num = list(map(int, input().split()))

print(num)
