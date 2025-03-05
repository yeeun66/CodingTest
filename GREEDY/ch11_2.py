# 이것이 코딩테스트다 책 - Ch11 그리디 기출문제 02번) 곱하기 혹은 더하기

# 두 수중 하나라도 1이하라면 +가 더 크고, 나머지는 *가 더 큰 값을 생성함

string = input()

result = int(string[0])
for i in range(1, len(string)) :
    num = int(string[i])
    if num <= 1 or result <= 1 : result += num
    else : result *= num
print(result)