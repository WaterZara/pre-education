"""
7. 1부터 100까지 수의 합을 계산하고 있다.
이 때 합이 최초로 1000을 넘게 하는 수가 무엇인지 코드를 만들고 답을 구하시오


<출력>
 45
"""

result = 0  # 합의 초기값 설정

for i in range(1, 101):     # 1부터 101미만의 수
    result = result + i

    if result > 1000:       # result 가 최초로 1000을 넘었을 때
        print(i)            # i 의 값을 출력
        break               # 반복문 탈출
