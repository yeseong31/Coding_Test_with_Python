# 럭키 스트레이트

# 정수 N(항상 짝수)
n = list(input())
length = len(n) // 2

result_left, result_right = 0, 0
for i in range(length):
    result_left += int(n[i])
    result_right += int(n[-i - 1])

if result_left == result_right:
    print('LUCKY')
else:
    print('READY')