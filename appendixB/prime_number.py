# 소수의 판별

# 가장 간단한 방법은 x를 2부터 x - 1까지의 모든 수로 나누어 보는 것이다.
# 만약 2부터 x - 1까지의 모든 자연수로 나누었을 때
# 나누어 떨어지는 수가 하나라도 존재하면 소수가 아니다.

def is_prime_number(x):
    for i in range(2, x - 1):
        if x % i == 0:
            return False
    return True

print(is_prime_number(4))
print(is_prime_number(7))

# 하지만 이 알고리즘의 시간 복잡도는 O(X)로 굉장히 비효율적이다.
# 알고리즘을 개선하기 위해서는 자연수의 약수가 가지는 특징을 파악하면 된다.

# 모든 약수에 대하여, 가운데 약수를 기준으로 하여 대칭적으로 2개씩
# 앞뒤로 묶어서 곱하면 본래의 수를 구할 수 있다.
# 즉 소수의 판별은 '가운데 약수까지만 나누어떨어지는지' 확인하면 된다.

def improved_is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

print(improved_is_prime_number(4))
print(improved_is_prime_number(7))

# 하나의 수가 아닌 전체 수의 범위 안에서 존재하는 모든 소수를 찾기 위해서는
# '에라토스테네스의 체' 알고리즘을 사용해야 한다.
