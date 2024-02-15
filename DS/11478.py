# 서로 다른 부분 문자열의 개수
# 집합과 맵

# 문자열 S가 주어졌을 때, S의 서로 다른 부분 문자열의 개수를 구하는 프로그램
# 부분 문자열은 S에서 연속된 일부분을 말하며, 길이가 1보다 크거나 같아야 한다.

# 전체 문자열을 1개로 자르고, 2개로 자르고, ... , n개로 자르고  각 갯수를 집합으로 넣는다. 그리고 그 집합 갯수 세면 끝

string = list(map(str, input()))

result = set()
for i in range(len(string)) :
    result.update(string[i])