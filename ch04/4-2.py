# 시각
# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는
# 모든 경우의 수를 구하는 프로그램을 작성하시오.

# 입력 조건
# - 첫째 줄이 정수 N이 입력된다. (0 <= N <= 23)
# 출력 조건
# - 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력한다.

# 입력 예시
# 5
# 출력 예시
# 11475

# -----------------------------------------------------------------------------------------------
n = int(input())

count = 0
for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)

# -----------------------------------------------------------------------------------------------
# '완전 탐색 유형'으로 분류되는 문제이다. 모든 시각의 경우를 하나씩 모두 세서 쉽게 풀 수 있는 문제다.
# 모든 경우는 86400가지밖에 존제하지 않기 때문에 파이썬의 문자열 연산을 이용하여 3의 유무를 확인해도 2초 안에 해결 가능
# 따라서 단순히 시각을 1씩 증가시키면서 3이 하나라도 포함되어 있는지 확인하면 될 것이다.
# 24 X 60 X 60가지의 경우를 3중 반복문을 이용하여 알아낼 수 있다.

# 완전 탐색 알고리즘은 비효율적인 시간 복잡도를 가지고 있으므로 데이터 개수가 큰 경우에 정상적으로 동작하지 않을 수 있다.
# 전체 데이터의 개수가 100만 개 이하일 때 완전 탐색을 사용하면 좋다.