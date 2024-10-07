# 문장이 주어졌을 때, 단어를 모두 뒤집어서 출력하는 프로그램을 작성하시오. 

# - - - - - 로직 - - - - - 
# 일단 전체 스트링 뒤집기
# 그럼 단어 배치까지 반대로 되어있으니까
    # 단어 단위로 뒤에서 부터 꺼내 출력
    # 이 때 단어 단위로 만들기: string.split() 후 리스트로 바꿔
n = int(input())

for _ in range(n) :
    string = input().strip()
    string = string[::-1]
    string = list(string.split())
    string = string[::-1]
    print(*string)