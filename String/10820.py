# 문자열 N개가 주어진다. 
# 이때, 문자열에 포함되어 있는 소문자, 대문자, 숫자, 공백의 개수를 구하는 프로그램을 작성하시오.

# 문자열을 문장 단위로 입력받기 (총 몇 문장인지 처음부터 알 수 없을 때)
#     - sys.stdin.readline을 사용해 한 줄씩 입력받음
#     - 입력받은 문자열에서 오른쪽 개행 문자('\n')를 제거
#     - 입력이 없으면 (빈 줄이 입력되면) 반복 종료
#     - EOFError는 코드 실행 환경에 따라 발생할 수 있으므로 try-except로 처리
#         EOF 에러는 sys.stdin.readline 호출 시 입력 스트림이 끝났을 때 발생
#     - try 내부에서 할 일 하기


import sys
input = sys.stdin.readline
while True : 
    try : 
        line = input().rstrip('\n')

        arr = [0 for _ in range(4)]
        if not line : break
        for i in line :
            if i.islower() : arr[0] += 1
            elif i.isupper() : arr[1] += 1
            elif i.isdigit() : arr[2] += 1
            elif i == " " : arr[3] += 1
        print(*arr)
    except EOFError:
        break