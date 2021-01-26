# [람다 표현식]
# - 함수를 매우 간단하게 작성하여 적용할 수 있다.
# - 파이썬의 정렬 라이브러리를 사용할 때, 정렬 기준(Key)을 설정할 때에도 자주 사용된다.

def add(a, b):
    return a + b

print(add(3, 7))

print((lambda a, b: a + b)(3, 7))