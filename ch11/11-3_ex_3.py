# 문자열 뒤집기(p.313)

data = input()
count0 = count1 = 0

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        if data[i + 1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))

# 입력 예시
# 0001100
# 출력 예시
# 1
