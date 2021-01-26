# [조건부 표현식 예시]

score = 85
result = "Success" if score >= 80 else "Fail"

print(result)

# 조건부 표현식은 리스트에 있는 원소의 값을 변경해서, 또 다른 리스트를 만들고자 할 때 매우 간결하게 사용할 수 있다.

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]
print(result)