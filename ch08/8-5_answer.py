# 1로 만들기 (p.217)

# 이 문제는 잘 알려진 다이나믹 프로그래밍 문제이다.
# 문제에서 요구하는 내용을 점화식으로 표현해보자.
# 점화식 끝에 1을 더해주는 이유는 함수의 호출 횟수를 구해야 하기 때문이다.

#     a(i) = min( a(i-1), a(i/2), a(i/3), a(i/5) ) + 1

# 실제 코드로 구현할 때는 1을 빼는 연산을 제외하고는 해당 수로 나누어떨어질 때에 한해서만 점화식을 적용할 수 있다.

# ---------------------------------------------------------------------------------------------------------------------
# 정수 X 입력받기
x = int(input())
# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 30001

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
for i in range(2, x + 1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i - 1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2]) + 1
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3]) + 1
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5]) + 1

print(d[x])
