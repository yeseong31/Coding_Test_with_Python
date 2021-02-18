# 문자열 재정렬

# 알파벳 대문자와 숫자로만 구성된 문자열이 입력
str = input()

lst_alpha = []
result = 0
for s in str:
    if s.isdigit():
        result += int(s)
    else:
        lst_alpha.append(s)

lst_alpha.sort()

for i in lst_alpha:
    print(i, end='')
print(result)

# 입력 예시
# K1KA5CB7
# 출력 예시
# ABCKK13

# 입력 예시
# AJKDLSI412K4JSJ9D
# 출력 예시
# ADDIJJJKKLSS20

# 2020.02.18
# 또 다른 풀이
s = sorted(list(input()))
n = 0
for i in range(len(s)):
    if s[i].isdigit():
        n += int(s[i])
        idx = i
    else:
        break
print(''.join(s[idx + 1:]), n, sep='')
