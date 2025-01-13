# 알파벳 개수
# 각 알파벳이 단어에 몇 개가 포함되어 있는지 구하는 프로그램을 작성
# 입력: baekjoon
# 출력: 1 1 0 0 1 0 0 0 0 1 1 0 0 1 2 0 0 0 0 0 0 0 0 0 0 0

# 1. 26개의 배열 만들어서 0으로 초기화
# 2. 문자열 입력 받고 하나씩 돌면서,
    # 해당 문자의 a와의 차이를 인덱스로 해서 배열의 해당 칸 +1
# 3. 배열 출력

import sys
input = sys.stdin.readline

string = input().strip()
arr = [0] * 26
for i in string : 
    index = ord(i) - ord('a')
    arr[index] += 1

print(*arr)