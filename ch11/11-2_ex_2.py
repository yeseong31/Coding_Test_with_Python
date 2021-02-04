# 곱하기 혹은 더하기(p.312)

s = list(input())

result = int(s[0])
for i in range(1, len(s)):
    n = int(s[i])
    if result <= 1 or n <= 1:
        result += n
    else:
        result *= n

print(result)

# 입력 예시 1
# 02984
# 출력 예시 1
# 576
#
# 입력 예시 2
# 567
# 출력 예시 2
# 210
