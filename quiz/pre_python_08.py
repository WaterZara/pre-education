"""
8. 정수를 입력했을 때 짝수인지 홀수인지 핀별하는 코드를 작성하시오

예시
<입력>
정수를 입력하세요 : 14

<출력>
짝수입니다.
"""


integer = int(input("정수를 입력하세요 : "))    # 정수 입력란

if integer % 2 == 1:    # 입력된 정수를 2로 나누었을 때 나머지가 1이라면
    print("홀수입니다.")  # 홀수 출력
else:                   # 1과 같지 않은 나머지
    print("짝수입니다.")  # 짝수 출력
