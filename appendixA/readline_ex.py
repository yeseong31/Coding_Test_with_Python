# 입력의 개수가 많은 경우에는 단순히 input() 함수를 그대로 사용하지는 않는다.
# 파이썬의 기본 input() 함수는 동작 속도가 느려서 시간 초과로 오답 판정을 받을 수 있기 때문이다.

# 이 경우 파이썬의 sys 라이브러리에 정의되어 있는 sys.stdin.readline() 함수를 이용한다.
import sys
data = sys.stdin.readline().rstrip()
print(data)

# sys 라이브러리를 사용할 때는 한 줄 읿력을 받고 나서 rstrip() 함수를 꼭 호출해야 한다.
# readline()으로 입력하면 <Enter>가 줄 바꿈 기호로 입력되는데,
# 이 공백 문자를 제거하려면 rstrip() 함수를 사용해야 한다. 관행적으로 외워서 사용하자.
